import numpy as np
from pydantic import BaseModel


class EphemeralitySet(BaseModel):
    """
    Container for ephemerality and core size values.

    This class is a simple pydantic BaseModel used to store computed core lengths and corresponding ephemerality values
    by core type. Values that were not computed default to None.

    Attributes
    ----------
    len_left_core : int, optional
        Length of the left core in time bins
    len_middle_core : int, optional
        Length of the middle core in time bins
    len_right_core : int, optional
        Length of the right core in time bins
    len_sorted_core : int, optional
        Length of the sorted core in time bins

    eph_left_core: float, optional
        Ephemerality value for the left core
    eph_middle_core: float, optional
        Ephemerality value for the middle core
    eph_right_core: float, optional
        Ephemerality value for the right core
    eph_sorted_core: float, optional
        Ephemerality value for the sorted core
    """
    len_left_core: int | None = None
    len_middle_core: int | None = None
    len_right_core: int | None = None
    len_sorted_core: int | None = None

    eph_left_core: float | None = None
    eph_middle_core: float | None = None
    eph_right_core: float | None = None
    eph_sorted_core: float | None = None

    def __eq__(self, other) -> bool:
        if isinstance(other, EphemeralitySet):
            if \
                    self.len_left_core != other.len_left_core or \
                    self.len_middle_core != other.len_middle_core or \
                    self.len_right_core != other.len_right_core or \
                    self.len_sorted_core != other.len_sorted_core or \
                    not self._cmp_float_none(self.eph_left_core, other.eph_left_core) or \
                    not self._cmp_float_none(self.eph_middle_core, other.eph_middle_core) or \
                    not self._cmp_float_none(self.eph_right_core, other.eph_right_core) or \
                    not self._cmp_float_none(self.eph_sorted_core, other.eph_sorted_core):
                return False
            else:
                return True
        else:
            return False

    @staticmethod
    def _cmp_float_none(value1: float | None, value2: float | None) -> bool:
        if value1 is None and value2 is None:
            return True
        elif value1 is None or value2 is None:
            return False
        else:
            return np.isclose(value1, value2)

    def __str__(self) -> str:
        values = ', '.join([f'{pair[0]}={pair[1]}' for pair in sorted(list(self.dict(exclude_none=True).items()), key=lambda x: x[0])])
        return f'{self.__class__.__name__}({values})'

    def __repr__(self) -> str:
        return str(self)
