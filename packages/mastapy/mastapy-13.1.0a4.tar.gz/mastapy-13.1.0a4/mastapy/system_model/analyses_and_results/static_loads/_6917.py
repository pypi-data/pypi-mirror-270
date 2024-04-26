"""GearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6951
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2548
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6918,
        _6840,
        _6849,
        _6852,
        _6853,
        _6854,
        _6868,
        _6871,
        _6888,
        _6893,
        _6911,
        _6932,
        _6939,
        _6942,
        _6945,
        _6980,
        _6986,
        _6989,
        _6992,
        _6993,
        _7009,
        _7012,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearLoadCase",)


Self = TypeVar("Self", bound="GearLoadCase")


class GearLoadCase(_6951.MountableComponentLoadCase):
    """GearLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearLoadCase")

    class _Cast_GearLoadCase:
        """Special nested class for casting GearLoadCase to subclasses."""

        def __init__(self: "GearLoadCase._Cast_GearLoadCase", parent: "GearLoadCase"):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6849.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6852.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6853.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6868.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6871.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConicalGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6888.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6893.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6911.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.FaceGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6932.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(
                _6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def spiral_bevel_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6980.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6986.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6989.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6992.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_6993.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.StraightBevelSunGearLoadCase)

        @property
        def worm_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_7009.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "GearLoadCase._Cast_GearLoadCase",
        ) -> "_7012.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7012

            return self._parent._cast(_7012.ZerolBevelGearLoadCase)

        @property
        def gear_load_case(self: "GearLoadCase._Cast_GearLoadCase") -> "GearLoadCase":
            return self._parent

        def __getattr__(self: "GearLoadCase._Cast_GearLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_temperature(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GearTemperature

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gear_temperature.setter
    @enforce_parameter_types
    def gear_temperature(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GearTemperature = value

    @property
    def component_design(self: Self) -> "_2548.Gear":
        """mastapy.system_model.part_model.gears.Gear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: Self) -> "_6918.GearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.GearManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearLoadCase._Cast_GearLoadCase":
        return self._Cast_GearLoadCase(self)
