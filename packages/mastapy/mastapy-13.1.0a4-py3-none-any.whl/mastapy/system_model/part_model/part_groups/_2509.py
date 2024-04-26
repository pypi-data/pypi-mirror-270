"""ParallelPartGroupSelection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.part_model.part_groups import _2508
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARALLEL_PART_GROUP_SELECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "ParallelPartGroupSelection"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2507, _2504, _2510


__docformat__ = "restructuredtext en"
__all__ = ("ParallelPartGroupSelection",)


Self = TypeVar("Self", bound="ParallelPartGroupSelection")


class ParallelPartGroupSelection(_2508.ParallelPartGroup):
    """ParallelPartGroupSelection

    This is a mastapy class.
    """

    TYPE = _PARALLEL_PART_GROUP_SELECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParallelPartGroupSelection")

    class _Cast_ParallelPartGroupSelection:
        """Special nested class for casting ParallelPartGroupSelection to subclasses."""

        def __init__(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
            parent: "ParallelPartGroupSelection",
        ):
            self._parent = parent

        @property
        def parallel_part_group(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
        ) -> "_2508.ParallelPartGroup":
            return self._parent._cast(_2508.ParallelPartGroup)

        @property
        def concentric_or_parallel_part_group(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
        ) -> "_2504.ConcentricOrParallelPartGroup":
            from mastapy.system_model.part_model.part_groups import _2504

            return self._parent._cast(_2504.ConcentricOrParallelPartGroup)

        @property
        def part_group(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
        ) -> "_2510.PartGroup":
            from mastapy.system_model.part_model.part_groups import _2510

            return self._parent._cast(_2510.PartGroup)

        @property
        def parallel_part_group_selection(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
        ) -> "ParallelPartGroupSelection":
            return self._parent

        def __getattr__(
            self: "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParallelPartGroupSelection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_measurements(self: Self) -> "List[_2507.DesignMeasurements]":
        """List[mastapy.system_model.part_model.part_groups.DesignMeasurements]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignMeasurements

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ParallelPartGroupSelection._Cast_ParallelPartGroupSelection":
        return self._Cast_ParallelPartGroupSelection(self)
