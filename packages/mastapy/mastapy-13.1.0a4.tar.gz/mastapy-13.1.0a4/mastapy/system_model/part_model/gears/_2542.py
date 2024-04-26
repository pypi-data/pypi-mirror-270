"""ConicalGearSet"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGearSet"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1166
    from mastapy.system_model.part_model.gears import (
        _2541,
        _2532,
        _2534,
        _2538,
        _2553,
        _2555,
        _2557,
        _2559,
        _2562,
        _2564,
        _2566,
        _2572,
    )
    from mastapy.system_model.part_model import _2494, _2452, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSet",)


Self = TypeVar("Self", bound="ConicalGearSet")


class ConicalGearSet(_2550.GearSet):
    """ConicalGearSet

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSet")

    class _Cast_ConicalGearSet:
        """Special nested class for casting ConicalGearSet to subclasses."""

        def __init__(
            self: "ConicalGearSet._Cast_ConicalGearSet", parent: "ConicalGearSet"
        ):
            self._parent = parent

        @property
        def gear_set(self: "ConicalGearSet._Cast_ConicalGearSet") -> "_2550.GearSet":
            return self._parent._cast(_2550.GearSet)

        @property
        def specialised_assembly(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2494.SpecialisedAssembly":
            from mastapy.system_model.part_model import _2494

            return self._parent._cast(_2494.SpecialisedAssembly)

        @property
        def abstract_assembly(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2452.AbstractAssembly":
            from mastapy.system_model.part_model import _2452

            return self._parent._cast(_2452.AbstractAssembly)

        @property
        def part(self: "ConicalGearSet._Cast_ConicalGearSet") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def agma_gleason_conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2532.AGMAGleasonConicalGearSet":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.AGMAGleasonConicalGearSet)

        @property
        def bevel_differential_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2534.BevelDifferentialGearSet":
            from mastapy.system_model.part_model.gears import _2534

            return self._parent._cast(_2534.BevelDifferentialGearSet)

        @property
        def bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2538.BevelGearSet":
            from mastapy.system_model.part_model.gears import _2538

            return self._parent._cast(_2538.BevelGearSet)

        @property
        def hypoid_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2553.HypoidGearSet":
            from mastapy.system_model.part_model.gears import _2553

            return self._parent._cast(_2553.HypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.KlingelnbergCycloPalloidConicalGearSet)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2557.KlingelnbergCycloPalloidHypoidGearSet":
            from mastapy.system_model.part_model.gears import _2557

            return self._parent._cast(_2557.KlingelnbergCycloPalloidHypoidGearSet)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2559

            return self._parent._cast(_2559.KlingelnbergCycloPalloidSpiralBevelGearSet)

        @property
        def spiral_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2562.SpiralBevelGearSet":
            from mastapy.system_model.part_model.gears import _2562

            return self._parent._cast(_2562.SpiralBevelGearSet)

        @property
        def straight_bevel_diff_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2564.StraightBevelDiffGearSet":
            from mastapy.system_model.part_model.gears import _2564

            return self._parent._cast(_2564.StraightBevelDiffGearSet)

        @property
        def straight_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2566.StraightBevelGearSet":
            from mastapy.system_model.part_model.gears import _2566

            return self._parent._cast(_2566.StraightBevelGearSet)

        @property
        def zerol_bevel_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "_2572.ZerolBevelGearSet":
            from mastapy.system_model.part_model.gears import _2572

            return self._parent._cast(_2572.ZerolBevelGearSet)

        @property
        def conical_gear_set(
            self: "ConicalGearSet._Cast_ConicalGearSet",
        ) -> "ConicalGearSet":
            return self._parent

        def __getattr__(self: "ConicalGearSet._Cast_ConicalGearSet", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSet.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self: Self) -> "_1166.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_set_design(self: Self) -> "_1166.ConicalGearSetDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears(self: Self) -> "List[_2541.ConicalGear]":
        """List[mastapy.system_model.part_model.gears.ConicalGear]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearSet._Cast_ConicalGearSet":
        return self._Cast_ConicalGearSet(self)
