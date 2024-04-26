"""BevelGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2532
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2534,
        _2562,
        _2564,
        _2566,
        _2572,
        _2542,
        _2550,
    )
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSet",)


Self = TypeVar("Self", bound="BevelGearSet")


class BevelGearSet(_2532.AGMAGleasonConicalGearSet):
    """BevelGearSet

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSet")

    class _Cast_BevelGearSet:
        """Special nested class for casting BevelGearSet to subclasses."""

        def __init__(self: "BevelGearSet._Cast_BevelGearSet", parent: "BevelGearSet"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def conical_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2542.ConicalGearSet":
            from mastapy.system_model.part_model.gears import _2542

            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def gear_set(self: "BevelGearSet._Cast_BevelGearSet") -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(self: "BevelGearSet._Cast_BevelGearSet") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2534.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.BevelDifferentialGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2562.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2564.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2566.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "BevelGearSet._Cast_BevelGearSet",
        ) -> "_2572.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.ZerolBevelGearSet)

        @property
        def bevel_gear_set(self: "BevelGearSet._Cast_BevelGearSet") -> "BevelGearSet":
            return self._parent

        def __getattr__(self: "BevelGearSet._Cast_BevelGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BevelGearSet._Cast_BevelGearSet":
        return self._Cast_BevelGearSet(self)
