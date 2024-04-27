from __future__ import annotations

from typing import TYPE_CHECKING

import numpy as np
from ase import Atoms
from ase.cell import Cell
from scipy.ndimage import maximum_filter
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components

from abtem.core.energy import energy2wavelength
from abtem.core.utils import label_to_index

if TYPE_CHECKING:
    from abtem.measurements import DiffractionPatterns


def _get_frequency_bin_edges(diffraction_patterns):
    bin_edge_x = np.fft.fftshift(
        np.fft.fftfreq(
            diffraction_patterns.shape[-2], d=1 / diffraction_patterns.shape[-2]
        )
    ).astype(int)
    bin_edge_y = np.fft.fftshift(
        np.fft.fftfreq(
            diffraction_patterns.shape[-1], d=1 / diffraction_patterns.shape[-1]
        )
    ).astype(int)
    bin_edge_x = (
        bin_edge_x * diffraction_patterns.sampling[0]
        - diffraction_patterns.sampling[0] / 2
    )
    bin_edge_y = (
        bin_edge_y * diffraction_patterns.sampling[1]
        - diffraction_patterns.sampling[1] / 2
    )
    return bin_edge_x, bin_edge_y


def _sphere_of_miller_index_grid_points(
    diffraction_patterns, cell=None, max_index=None
):
    if max_index is None:
        if cell is None:
            raise RuntimeError()

        min_planar_distance = cell.reciprocal().lengths().min()
        max_limit = max(
            (
                abs(diffraction_patterns.limits[0][0]),
                abs(diffraction_patterns.limits[1][0]),
            )
        )
        max_index = int(np.ceil(max_limit / min_planar_distance))

    hkl = np.meshgrid(*(np.arange(-max_index, max_index + 1),) * 3, indexing="ij")
    hkl = np.stack((hkl[0], hkl[1], hkl[2]), -1).reshape((-1, 3))

    return hkl[np.linalg.norm(hkl, axis=-1) < max_index]


def _k_space_grid_points(hkl, cell):
    k = (
        hkl[:, 0, None] * cell.reciprocal()[0, None]
        + hkl[:, 1, None] * cell.reciprocal()[1, None]
        + hkl[:, 2, None] * cell.reciprocal()[2, None]
    )
    return k


def _sagita(radius, chord):
    return radius - np.sqrt(radius**2 - (chord / 2) ** 2)


def _digitize_k_space_grid(k_grid, diffraction_patterns):
    bin_edge_x, bin_edge_y = _get_frequency_bin_edges(diffraction_patterns)

    n = np.digitize(k_grid[:, 0], bin_edge_x) - 1
    m = np.digitize(k_grid[:, 1], bin_edge_y) - 1

    nm = np.concatenate((n[:, None], m[:, None]), axis=1)

    return nm


def _k_space_distances_to_ewald_sphere(k_grid, wavelength):
    k_norm = np.linalg.norm(k_grid[:, :2], axis=1)
    ewald_z = _sagita(1 / wavelength, k_norm * 2)
    return ewald_z - k_grid[:, 2]


def _validate_cell(cell: Atoms | Cell | float | tuple[float, float, float]) -> Cell:
    if isinstance(cell, Atoms):
        cell = cell.cell

    if np.isscalar(cell):
        cell = [cell] * 3

    if not isinstance(cell, Cell):
        cell = Cell(np.diag(cell))

    # if not is_cell_orthogonal(cell):
    #
    #     cell = Atoms(cell=cell)
    #     cell = abtem.orthogonalize_cell(cell).cell

    return cell


def _disk(width: int, height: int) -> np.ndarray:
    h = np.linspace(-1 + 1 / width, 1 - 1 / width, width)
    w = np.linspace(-1 + 1 / height, 1 - 1 / height, height)
    x, y = np.meshgrid(h, w, indexing="ij")
    return np.array((x**2 + y**2) <= 1.0, dtype=bool)


def _hkl_tuples_to_str(miller_indices):
    return ["{} {} {}".format(*hkl) for hkl in miller_indices]


def _hkl_str_to_tuples(miller_indices):
    return [tuple(int(index) for index in hkl.split(" ")) for hkl in miller_indices]


def _integrate_disk(array, center, footprint):

    radius = footprint.shape[0] // 2, footprint.shape[1] // 2
    slice_limits = [
        (
            max(center[i] - radius[i], 0),
            min(center[i] + radius[i] + 1, array.shape[-2 + i]),
        )
        for i in range(2)
    ]

    mask_slice_limits = [
        (
            slice_limits[i][0] - (center[i] - radius[i]),
            footprint.shape[i] + (slice_limits[i][1] - (center[i] + radius[i] + 1)),
        )
        for i in range(2)
    ]
    cropped = array[..., slice(*slice_limits[0]), slice(*slice_limits[1])]
    cropped_integration_footprint = footprint[
        slice(*mask_slice_limits[0]), slice(*mask_slice_limits[1])
    ]

    return (cropped * cropped_integration_footprint).sum((-2, -1))


def _F_reflection_conditions(hkl):
    all_even = (hkl % 2 == 0).all(axis=1)
    all_odd = (hkl % 2 == 1).all(axis=1)
    return all_even + all_odd


def _I_reflection_conditions(hkl):
    return (hkl.sum(axis=1) % 2 == 0).all(axis=1)


def _A_reflection_conditions(hkl):
    return (hkl[1:].sum(axis=1) % 2 == 0).all(axis=1)


def _B_reflection_conditions(hkl):
    return (hkl[:, [0, 1]].sum(axis=1) % 2 == 0).all(axis=1)


def _C_reflection_conditions(hkl):
    return (hkl[:-1].sum(axis=1) % 2 == 0).all(axis=1)


def _reflection_condition_mask(hkl: np.ndarray, centering: str):

    if centering == "P":
        return np.ones(len(hkl), dtype=bool)
    elif centering == "F":
        return _F_reflection_conditions(hkl)
    elif centering == "I":
        return _I_reflection_conditions(hkl)
    elif centering == "A":
        return _A_reflection_conditions(hkl)
    elif centering == "B":
        return _B_reflection_conditions(hkl)
    elif centering == "C":
        return _C_reflection_conditions(hkl)
    else:
        raise ValueError("lattice centering must be one of P, I, F, A, B or C")


def _index_diffraction_patterns(
    diffraction_patterns: DiffractionPatterns,
    cell: Atoms | Cell | float | tuple[float, float, float],
    threshold: float,
    distance_threshold: float,
    min_distance: float = 0.0,
    integration_radius: float = 0.0,
    max_index: int = None,
    centering: str = "P",
):
    cell = _validate_cell(cell)

    shape = diffraction_patterns.shape[-2:]

    hkl = _sphere_of_miller_index_grid_points(diffraction_patterns, cell, max_index)

    mask = _reflection_condition_mask(hkl, centering=centering)
    hkl = hkl[mask]

    k = _k_space_grid_points(hkl, cell)

    mask = (
        (k[:, 0] >= diffraction_patterns.limits[0][0])
        * (k[:, 0] <= diffraction_patterns.limits[0][1])
        * (k[:, 1] >= diffraction_patterns.limits[1][0])
        * (k[:, 1] <= diffraction_patterns.limits[1][1])
    )

    k = k[mask]
    hkl = hkl[mask]

    wavelength = energy2wavelength(diffraction_patterns._get_from_metadata("energy"))
    d_ewald = np.abs(_k_space_distances_to_ewald_sphere(k, wavelength))

    mask = d_ewald < distance_threshold

    k = k[mask]
    hkl = hkl[mask]
    d_ewald = d_ewald[mask]

    nm = _digitize_k_space_grid(k, diffraction_patterns)
    labels = np.ravel_multi_index(nm.T, shape)

    ensemble_indices = tuple(range(len(diffraction_patterns.ensemble_shape)))
    max_intensities = diffraction_patterns.array.max(axis=ensemble_indices)

    if min_distance:
        size = (
            np.ceil((min_distance / np.array(diffraction_patterns.sampling))) // 2 * 4
            + 1
        ).astype(int)

        footprint = _disk(*size)
        maximum_filtered = maximum_filter(
            max_intensities, footprint=footprint, mode="constant"
        )
    else:
        maximum_filtered = None

    if integration_radius:
        size = (
            np.ceil((2 * integration_radius / np.array(diffraction_patterns.sampling)))
            // 2
            * 2
            + 1
        ).astype(int)

        integration_footprint = _disk(*size)
    else:
        integration_footprint = None

    selected_hkl = []
    intensities = []
    positions = []
    for label, indices in enumerate(label_to_index(labels)):

        if len(indices) == 0:
            continue

        n, m = np.unravel_index(label, shape)

        max_intensity = max_intensities[n, m]

        if maximum_filtered is not None:
            if max_intensity != maximum_filtered[n, m]:
                continue

        if integration_footprint is not None:
            max_intensity = _integrate_disk(
                max_intensities, (n, m), integration_footprint
            )

        if max_intensity < threshold:
            continue

        min_index = np.argmin(d_ewald[indices])

        selected_hkl.append(hkl[indices][min_index])

        if integration_footprint is not None:
            intensities.append(
                _integrate_disk(
                    diffraction_patterns.array, (n, m), integration_footprint
                )
            )
        else:
            intensities.append(diffraction_patterns.array[..., n, m])

        positions.append(k[indices][min_index])

    intensities = np.array(intensities)

    if intensities.size == 0:
        raise RuntimeError("no diffraction spots found within provided threshold")

    intensities = np.moveaxis(intensities, 0, -1)

    return np.array(selected_hkl), intensities, np.array(positions)


def _format_miller_indices(hkl):
    return "{} {} {}".format(*hkl)


def _miller_to_miller_bravais(hkl):
    h, k, l = hkl

    H = 2 * h - k
    K = 2 * k - h
    I = -H - K
    L = l

    return H, K, I, L


def _equivalent_miller_indices(hkl):
    is_negation = np.zeros((len(hkl), len(hkl)), dtype=bool)

    for i in range(hkl.shape[1]):
        negated = hkl.copy()
        negated[:, i] = -negated[:, i]
        is_negation += np.all(hkl[:, None] == negated[None], axis=2)

    is_negation += np.all(hkl[:, None] == -hkl[None], axis=2)

    sorted = np.sort(hkl, axis=1)
    is_permutation = np.all(sorted[:, None] == sorted[None], axis=-1)

    is_connected = is_negation + is_permutation
    n, labels = connected_components(csr_matrix(is_connected))
    return labels


def _split_at_threshold(values, threshold):
    order = np.argsort(values)
    max_value = values.max()

    split = (np.diff(values[order]) > (max_value * threshold)) * (
        np.diff(values[order]) > 1e-6
    )

    split = np.insert(split, 0, False)
    return np.cumsum(split)[np.argsort(order)]


def _find_equivalent_spots(hkl, intensities, intensity_split: float = 1.0):
    labels = _equivalent_miller_indices(hkl)

    spots = np.zeros(len(hkl), dtype=bool)
    for indices in label_to_index(labels):
        sub_labels = _split_at_threshold(intensities[indices], intensity_split)
        for sub_indices in label_to_index(sub_labels):
            order = np.lexsort(np.rot90(hkl[indices][sub_indices]))
            spots[indices[sub_indices[order][-1]]] = True

    return spots
