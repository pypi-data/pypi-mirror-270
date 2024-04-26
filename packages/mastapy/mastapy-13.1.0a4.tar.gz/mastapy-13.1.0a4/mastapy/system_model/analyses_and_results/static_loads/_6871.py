"""ConicalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6917
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6872,
        _6840,
        _6849,
        _6852,
        _6853,
        _6854,
        _6932,
        _6939,
        _6942,
        _6945,
        _6980,
        _6986,
        _6989,
        _6992,
        _6993,
        _7012,
        _6951,
        _6864,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLoadCase",)


Self = TypeVar("Self", bound="ConicalGearLoadCase")


class ConicalGearLoadCase(_6917.GearLoadCase):
    """ConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLoadCase")

    class _Cast_ConicalGearLoadCase:
        """Special nested class for casting ConicalGearLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
            parent: "ConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6917.GearLoadCase":
            return self._parent._cast(_6917.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6951.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6864.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6849.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6852.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6853.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6932.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(
                _6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6980.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6986.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6989.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6992.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6993.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_7012.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7012

            return self._parent._cast(_7012.ZerolBevelGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "ConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2541.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: Self) -> "_6872.ConicalGearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearLoadCase._Cast_ConicalGearLoadCase":
        return self._Cast_ConicalGearLoadCase(self)
