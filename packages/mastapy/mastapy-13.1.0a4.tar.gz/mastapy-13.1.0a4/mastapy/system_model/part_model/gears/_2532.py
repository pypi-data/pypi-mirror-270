"""AGMAGleasonConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model.gears import _2542
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "AGMAGleasonConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2534,
        _2538,
        _2553,
        _2562,
        _2564,
        _2566,
        _2572,
        _2550,
    )
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSet",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSet")


class AGMAGleasonConicalGearSet(_2542.ConicalGearSet):
    """AGMAGleasonConicalGearSet

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSet")

    class _Cast_AGMAGleasonConicalGearSet:
        """Special nested class for casting AGMAGleasonConicalGearSet to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
            parent: "AGMAGleasonConicalGearSet",
        ):
            self._parent = parent

        @property
        def conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2542.ConicalGearSet":
            return self._parent._cast(_2542.ConicalGearSet)

        @property
        def gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2550.GearSet":
            from mastapy.system_model.part_model.gears import _2550

            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def bevel_differential_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2534.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2538.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2553.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.HypoidGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2562.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2564.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2566.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "_2572.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.ZerolBevelGearSet)

        @property
        def agma_gleason_conical_gear_set(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet",
        ) -> "AGMAGleasonConicalGearSet":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSet._Cast_AGMAGleasonConicalGearSet":
        return self._Cast_AGMAGleasonConicalGearSet(self)
