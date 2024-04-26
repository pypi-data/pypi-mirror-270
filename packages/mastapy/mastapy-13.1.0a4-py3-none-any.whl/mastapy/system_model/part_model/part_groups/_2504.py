"""ConcentricOrParallelPartGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.part_groups import _2510
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCENTRIC_OR_PARALLEL_PART_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.PartGroups", "ConcentricOrParallelPartGroup"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.part_groups import _2505, _2508, _2509


__docformat__ = "restructuredtext en"
__all__ = ("ConcentricOrParallelPartGroup",)


Self = TypeVar("Self", bound="ConcentricOrParallelPartGroup")


class ConcentricOrParallelPartGroup(_2510.PartGroup):
    """ConcentricOrParallelPartGroup

    This is a mastapy class.
    """

    TYPE = _CONCENTRIC_OR_PARALLEL_PART_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConcentricOrParallelPartGroup")

    class _Cast_ConcentricOrParallelPartGroup:
        """Special nested class for casting ConcentricOrParallelPartGroup to subclasses."""

        def __init__(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
            parent: "ConcentricOrParallelPartGroup",
        ):
            self._parent = parent

        @property
        def part_group(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
        ) -> "_2510.PartGroup":
            return self._parent._cast(_2510.PartGroup)

        @property
        def concentric_part_group(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
        ) -> "_2505.ConcentricPartGroup":
            from mastapy.system_model.part_model.part_groups import _2505

            return self._parent._cast(_2505.ConcentricPartGroup)

        @property
        def parallel_part_group(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
        ) -> "_2508.ParallelPartGroup":
            from mastapy.system_model.part_model.part_groups import _2508

            return self._parent._cast(_2508.ParallelPartGroup)

        @property
        def parallel_part_group_selection(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
        ) -> "_2509.ParallelPartGroupSelection":
            from mastapy.system_model.part_model.part_groups import _2509

            return self._parent._cast(_2509.ParallelPartGroupSelection)

        @property
        def concentric_or_parallel_part_group(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
        ) -> "ConcentricOrParallelPartGroup":
            return self._parent

        def __getattr__(
            self: "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConcentricOrParallelPartGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConcentricOrParallelPartGroup._Cast_ConcentricOrParallelPartGroup":
        return self._Cast_ConcentricOrParallelPartGroup(self)
