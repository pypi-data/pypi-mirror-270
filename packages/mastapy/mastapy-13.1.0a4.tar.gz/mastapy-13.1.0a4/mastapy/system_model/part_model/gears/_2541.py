"""ConicalGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "ConicalGear"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import (
        _2549,
        _2531,
        _2533,
        _2535,
        _2536,
        _2537,
        _2552,
        _2554,
        _2556,
        _2558,
        _2561,
        _2563,
        _2565,
        _2567,
        _2568,
        _2571,
    )
    from mastapy.gears.gear_designs.conical import _1164
    from mastapy.system_model.part_model import _2482, _2462, _2486
    from mastapy.system_model import _2221


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGear",)


Self = TypeVar("Self", bound="ConicalGear")


class ConicalGear(_2548.Gear):
    """ConicalGear

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGear")

    class _Cast_ConicalGear:
        """Special nested class for casting ConicalGear to subclasses."""

        def __init__(self: "ConicalGear._Cast_ConicalGear", parent: "ConicalGear"):
            self._parent = parent

        @property
        def gear(self: "ConicalGear._Cast_ConicalGear") -> "_2548.Gear":
            return self._parent._cast(_2548.Gear)

        @property
        def mountable_component(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2482.MountableComponent":
            from mastapy.system_model.part_model import _2482

            return self._parent._cast(_2482.MountableComponent)

        @property
        def component(self: "ConicalGear._Cast_ConicalGear") -> "_2462.Component":
            from mastapy.system_model.part_model import _2462

            return self._parent._cast(_2462.Component)

        @property
        def part(self: "ConicalGear._Cast_ConicalGear") -> "_2486.Part":
            from mastapy.system_model.part_model import _2486

            return self._parent._cast(_2486.Part)

        @property
        def design_entity(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2221.DesignEntity":
            from mastapy.system_model import _2221

            return self._parent._cast(_2221.DesignEntity)

        @property
        def agma_gleason_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2531.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2531

            return self._parent._cast(_2531.AGMAGleasonConicalGear)

        @property
        def bevel_differential_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2533.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2533

            return self._parent._cast(_2533.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2535.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2535

            return self._parent._cast(_2535.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2536.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2536

            return self._parent._cast(_2536.BevelDifferentialSunGear)

        @property
        def bevel_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2537.BevelGear":
            from mastapy.system_model.part_model.gears import _2537

            return self._parent._cast(_2537.BevelGear)

        @property
        def hypoid_gear(self: "ConicalGear._Cast_ConicalGear") -> "_2552.HypoidGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.HypoidGear)

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2554.KlingelnbergCycloPalloidConicalGear":
            from mastapy.system_model.part_model.gears import _2554

            return self._parent._cast(_2554.KlingelnbergCycloPalloidConicalGear)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
            from mastapy.system_model.part_model.gears import _2556

            return self._parent._cast(_2556.KlingelnbergCycloPalloidHypoidGear)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2558

            return self._parent._cast(_2558.KlingelnbergCycloPalloidSpiralBevelGear)

        @property
        def spiral_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2561.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2561

            return self._parent._cast(_2561.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2563.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2563

            return self._parent._cast(_2563.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2565.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2565

            return self._parent._cast(_2565.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2567.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2567

            return self._parent._cast(_2567.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2568.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2568

            return self._parent._cast(_2568.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "ConicalGear._Cast_ConicalGear",
        ) -> "_2571.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2571

            return self._parent._cast(_2571.ZerolBevelGear)

        @property
        def conical_gear(self: "ConicalGear._Cast_ConicalGear") -> "ConicalGear":
            return self._parent

        def __getattr__(self: "ConicalGear._Cast_ConicalGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Length

        if temp is None:
            return 0.0

        return temp

    @property
    def orientation(self: Self) -> "_2549.GearOrientations":
        """mastapy.system_model.part_model.gears.GearOrientations"""
        temp = self.wrapped.Orientation

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.part_model.gears._2549", "GearOrientations"
        )(value)

    @orientation.setter
    @enforce_parameter_types
    def orientation(self: Self, value: "_2549.GearOrientations"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.PartModel.Gears.GearOrientations"
        )
        self.wrapped.Orientation = value

    @property
    def active_gear_design(self: Self) -> "_1164.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gear_design(self: Self) -> "_1164.ConicalGearDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConicalGear._Cast_ConicalGear":
        return self._Cast_ConicalGear(self)
