from typing import Sequence

import numpy as np
from numpy.typing import NDArray
from matplotlib import pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from .utils import EphemeralitySet


def _check_threshold(threshold: float) -> bool:
    if threshold <= 0.:
        raise ValueError('Threshold value must be greater than 0!')

    if threshold > 1.:
        raise ValueError('Threshold value must be less or equal to 1!')

    return True


def _ephemerality_raise_error(threshold: float) -> None:
    if _check_threshold(threshold):
        raise ValueError('Input activity vector has not been internally normalized (problematic data format?)!')


def _normalize_activity_vector(activity_vector: Sequence[float]) -> NDArray:
    activity_vector = np.array(activity_vector, dtype=np.float64)

    if sum(activity_vector) != 1.:
        activity_vector /= np.sum(activity_vector)
        
    return activity_vector


def _str_to_core_types(type_str: str) -> tuple[set[str], int]:
    types = set()
    for c in type_str.lower():
        match c:
            case 'l':
                types.add('l')
            case 'm':
                types.add('m')
            case 'r':
                types.add('r')
            case 's':
                types.add('s')
            case _:
                raise ValueError(f'Unrecognized core type: {c}')
    n_types = len(types)
    return types, n_types


def _init_fig(core_types: set[str]) -> tuple[Figure, list[Axes]]:
    fig = plt.figure()
    n_cores = len(core_types)
    axes = list()
    match n_cores:
        case 1:
            gs = fig.add_gridspec(nrows=1, ncols=1)
            grid = [gs[0, 0]]
        case 2:
            gs = fig.add_gridspec(nrows=1, ncols=2)
            grid = [gs[0, 0], gs[0, 1]]
        case 3:
            gs = fig.add_gridspec(nrows=2, ncols=1)
            gs_0 = gs[0].subgridspec(nrows=1, ncols=2)
            gs_1 = gs[1].subgridspec(nrows=1, ncols=3, width_ratios=[1, 2, 1])
            grid = [gs_0[0, 0], gs_0[0, 1], gs_1[0, 1]]
        case 4:
            gs = fig.add_gridspec(nrows=2, ncols=2)
            grid = [gs[0, 0], gs[0, 1], gs[1, 0], gs[1, 1]]
    for i in range(n_cores):
        axes.append(fig.add_subplot(grid[i]))

    return fig, axes


def _annotate_ax(ax: Axes, x_len: int, core_type: str, core_length: int, ephemerality: float, threshold: float) -> Axes:
    ax.set_xlim((0, x_len))
    ax.set_xlabel('Time')
    ax.set_ylabel('Normalized activity')
    ax.set_title(rf'{core_type} core (length {core_length}), $\varepsilon_{{{threshold}}}^{core_type[0].lower()}={np.round(ephemerality, 3)}$')
    return ax


def compute_left_core_length(activity_vector: NDArray, threshold: float, axes: Axes | None = None) -> int:
    """
    Compute the length of the left core of the activity vector.

    Parameters
    ----------
    activity_vector : numpy.typing.NDArray
        A normalized sequence of activity values. Time bins corresponding to each value is assumed to be of equal
        length.
    threshold : float
        Ratio of activity that is considered to comprise its core part.
    axes : Optional[Axes]
        If provided, will plot the histogram of the activity vector and color its core part on it.

    Returns
    -------
    int
        The length of the left core period of the activity vector.
    """
    current_sum = 0
    for i, freq in enumerate(activity_vector):
        current_sum = current_sum + freq
        if np.isclose(current_sum, threshold) or current_sum > threshold:
            if axes is not None:
                axes.stairs(activity_vector[:(i + 1)], np.arange(i + 2), fill=True, color='C1')
                axes.stairs(activity_vector, np.arange(len(activity_vector) + 1), fill=False, color='C0')
            return i + 1

    _ephemerality_raise_error(threshold)


def compute_right_core_length(activity_vector: NDArray, threshold: float, axes: Axes | None = None) -> int:
    """
    Compute the length of the right core of the activity vector.

    Parameters
    ----------
    activity_vector : numpy.typing.NDArray
        A normalized sequence of activity values. Time bins corresponding to each value is assumed to be of equal
        length.
    threshold : float
        Ratio of activity that is considered to comprise its core part.
    axes : Optional[Axes]
        If provided, will plot the histogram of the activity vector and color its core part on it.

    Returns
    -------
    int
        The length of the right core period of the activity vector.
    """
    current_sum = 0
    for i, freq in enumerate(activity_vector[::-1]):
        current_sum = current_sum + freq
        if np.isclose(current_sum, threshold) or current_sum > threshold:
            if axes is not None:
                bound = len(activity_vector) - (i + 1)
                axes.stairs(activity_vector[bound:], np.arange(bound, len(activity_vector) + 1), fill=True, color='C1')
                axes.stairs(activity_vector, np.arange(len(activity_vector) + 1), fill=False, color='C0')
            return i + 1

    _ephemerality_raise_error(threshold)


def compute_middle_core_length(activity_vector: NDArray, threshold: float, axes: Axes | None = None) -> int:
    """
    Compute the length of the middle core of the activity vector.

    Parameters
    ----------
    activity_vector : numpy.typing.NDArray
        A normalized sequence of activity values. Time bins corresponding to each value is assumed to be of equal
        length.
    threshold : float
        Ratio of activity that is considered to comprise its core part.
    axes : Optional[Axes]
        If provided, will plot the histogram of the activity vector and color its core part on it.

    Returns
    -------
    int
        The length of the middle core period of the activity vector.
    """
    lower_threshold = (1. - threshold) / 2

    current_left_sum = 0
    start_index = -1
    for i, freq in enumerate(activity_vector):
        current_left_sum += freq
        if current_left_sum > lower_threshold and not np.isclose(current_left_sum, lower_threshold):
            start_index = i
            break

    current_sum = 0
    for j, freq in enumerate(activity_vector[start_index:]):
        current_sum += freq
        if np.isclose(current_sum, threshold) or current_sum > threshold:
            if axes is not None:
                axes.stairs(activity_vector[start_index:(start_index + j + 1)], np.arange(start_index, start_index + j + 2), fill=True, color='C1')
                axes.stairs(activity_vector, np.arange(len(activity_vector) + 1), fill=False, color='C0')
            return j + 1

    _ephemerality_raise_error(threshold)


def compute_sorted_core_length(activity_vector: np.array, threshold: float, axes: Axes | None = None) -> int:
    """
    Compute the length of the sorted core of the activity vector.

    Parameters
    ----------
    activity_vector : numpy.typing.NDArray
        A normalized sequence of activity values. Time bins corresponding to each value is assumed to be of equal
        length.
    threshold : float
        Ratio of activity that is considered to comprise its core part.
    axes : Optional[Axes]
        If provided, will plot the histogram of the activity vector and color its core part on it.

    Returns
    -------
    int
        The length of the sorted core period of the activity vector.
    """
    indices = np.argsort(activity_vector)[::-1]
    freq_descending_order = activity_vector[indices]

    current_sum = 0
    for i, freq in enumerate(freq_descending_order):
        current_sum += freq
        if np.isclose(current_sum, threshold) or current_sum > threshold:
            if axes is not None:
                core = np.zeros((len(activity_vector),))
                core[indices[:(i + 1)]] = activity_vector[indices[:(i + 1)]]
                axes.stairs(core, np.arange(len(activity_vector) + 1), fill=True, color='C1')

                axes.stairs(activity_vector, np.arange(len(activity_vector) + 1), fill=False, color='C0')
            return i + 1

    _ephemerality_raise_error(threshold)


def _compute_ephemerality_from_core(core_length: int, range_length: int, threshold: float) -> float:
    return max(0., 1 - (core_length / range_length) / threshold)


def _plot(axes: list[Axes]) -> None:
    fig = plt.figure()
    n_cores = len(axes)


def compute_ephemerality(
        activity_vector: Sequence[float | int],
        threshold: float = 0.8,
        types: str = 'lmrs',
        plot: bool = False) -> EphemeralitySet:
    """Compute ephemerality values for given activity vector.

    This function computes ephemerality for a numeric vector using all current definitions of actiovity cores.
    Alpha (desired non-ephemeral core length) can be specified with ``threshold parameter. In case not all cores are
     needed, the required types can be specified in ``types``.

    Parameters
    ----------
    activity_vector : Sequence[float | int]
        A sequence of activity values. Time bins corresponding to each value is assumed to be of equal length. Does not
        need to be normalised.
    threshold : float, default=0.8
        Desired non-ephemeral core length as fraction. Ephemerality is equal to 1.0 if the core length is at least ``threshold`` of
        the ``activity_vector`` length.
    types : str, default='lmrs'
        Activity cores to be computed. A sequence of characters corresponding to core types.
        'l' for left core, 'm' for middle core, 'r' for right core, 's' for sorted core. Multiples of the same character
         will be ignored.
    plot : bool, default=False
        Set to True to display the activity over time plot with core periods highlighted.

    Returns
    -------
    EphemeralitySet
        Container for the computed core lengths and ephemerality values
    """
    _check_threshold(threshold)

    if np.sum(activity_vector) == 0.:
        raise ZeroDivisionError("Activity vector's sum is 0!")
    types, n_cores = _str_to_core_types(types)
    
    activity_vector = _normalize_activity_vector(activity_vector)
    len_range = len(activity_vector)

    if plot:
        fig, axes = _init_fig(types)
    else:
        axes = None
    subplot_types = list()

    core_ind = 0
    if 'l' in types:
        ax = axes[core_ind] if plot else None
        subplot_types.append('l')
        length_left_core = compute_left_core_length(activity_vector, threshold, axes=ax)
        ephemerality_left_core = _compute_ephemerality_from_core(length_left_core, len_range, threshold)
        core_ind += 1
    else:
        length_left_core = None
        ephemerality_left_core = None

    if 'm' in types:
        ax = axes[core_ind] if plot else None
        subplot_types.append('m')
        length_middle_core = compute_middle_core_length(activity_vector, threshold, axes=ax)
        ephemerality_middle_core = _compute_ephemerality_from_core(length_middle_core, len_range, threshold)
        core_ind += 1
    else:
        length_middle_core = None
        ephemerality_middle_core = None

    if 'r' in types:
        ax = axes[core_ind] if plot else None
        subplot_types.append('r')
        length_right_core = compute_right_core_length(activity_vector, threshold, axes=ax)
        ephemerality_right_core = _compute_ephemerality_from_core(length_right_core, len_range, threshold)
        core_ind += 1
    else:
        length_right_core = None
        ephemerality_right_core = None

    if 's' in types:
        ax = axes[core_ind] if plot else None
        subplot_types.append('s')
        length_sorted_core = compute_sorted_core_length(activity_vector, threshold, axes=ax)
        ephemerality_sorted_core = _compute_ephemerality_from_core(length_sorted_core, len_range, threshold)
        core_ind += 1
    else:
        length_sorted_core = None
        ephemerality_sorted_core = None

    if n_cores == 0:
        raise ValueError('No valid ephemerality cores requested!')

    ephemeralities = EphemeralitySet(
        len_left_core=length_left_core,
        len_middle_core=length_middle_core,
        len_right_core=length_right_core,
        len_sorted_core=length_sorted_core,

        eph_left_core=ephemerality_left_core,
        eph_middle_core=ephemerality_middle_core,
        eph_right_core=ephemerality_right_core,
        eph_sorted_core=ephemerality_sorted_core
    )

    if plot:
        for i, subplot_type in enumerate(subplot_types):
            match subplot_type:
                case 'l':
                    _annotate_ax(axes[i], len_range, 'Left', ephemeralities.len_left_core, ephemeralities.eph_left_core, threshold)
                case 'm':
                    _annotate_ax(axes[i], len_range, 'Middle', ephemeralities.len_middle_core, ephemeralities.eph_middle_core, threshold)
                case 'r':
                    _annotate_ax(axes[i], len_range, 'Right', ephemeralities.len_right_core, ephemeralities.eph_right_core, threshold)
                case 's':
                    _annotate_ax(axes[i], len_range, 'Sorted', ephemeralities.len_sorted_core, ephemeralities.eph_sorted_core, threshold)
        fig.tight_layout()
        fig.show()

    return ephemeralities
