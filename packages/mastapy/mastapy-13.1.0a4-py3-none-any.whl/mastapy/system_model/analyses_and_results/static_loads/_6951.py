"""MountableComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "MountableComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6840,
        _6846,
        _6849,
        _6852,
        _6853,
        _6854,
        _6860,
        _6866,
        _6868,
        _6871,
        _6877,
        _6879,
        _6883,
        _6888,
        _6893,
        _6911,
        _6917,
        _6932,
        _6939,
        _6942,
        _6945,
        _6948,
        _6949,
        _6953,
        _6957,
        _6962,
        _6965,
        _6966,
        _6967,
        _6970,
        _6974,
        _6976,
        _6980,
        _6984,
        _6986,
        _6989,
        _6992,
        _6993,
        _6994,
        _6996,
        _6997,
        _7001,
        _7002,
        _7007,
        _7008,
        _7009,
        _7012,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentLoadCase",)


Self = TypeVar("Self", bound="MountableComponentLoadCase")


class MountableComponentLoadCase(_6864.ComponentLoadCase):
    """MountableComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentLoadCase")

    class _Cast_MountableComponentLoadCase:
        """Special nested class for casting MountableComponentLoadCase to subclasses."""

        def __init__(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
            parent: "MountableComponentLoadCase",
        ):
            self._parent = parent

        @property
        def component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6864.ComponentLoadCase":
            return self._parent._cast(_6864.ComponentLoadCase)

        @property
        def part_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6840.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6846.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6849.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6852.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6853.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6854.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.BevelGearLoadCase)

        @property
        def clutch_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6860.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6866.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6868.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6871.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6871

            return self._parent._cast(_6871.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6877.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6877

            return self._parent._cast(_6877.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6879.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6879

            return self._parent._cast(_6879.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6883.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6883

            return self._parent._cast(_6883.CVTPulleyLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6888.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6893.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.CylindricalPlanetGearLoadCase)

        @property
        def face_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6911.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6911

            return self._parent._cast(_6911.FaceGearLoadCase)

        @property
        def gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6917.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(_6917.GearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6932.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6939.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6939

            return self._parent._cast(_6939.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6942.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6945

            return self._parent._cast(
                _6945.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6948.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6949.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.MeasurementComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6953.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6957.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6962.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6965.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6966.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6967.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6970.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6974.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6974

            return self._parent._cast(_6974.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6976.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.ShaftHubConnectionLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6980.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6980

            return self._parent._cast(_6980.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6984.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6986.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6989.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6992.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6992

            return self._parent._cast(_6992.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6993.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6993

            return self._parent._cast(_6993.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6994.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6994

            return self._parent._cast(_6994.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6996.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6996

            return self._parent._cast(_6996.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_6997.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6997

            return self._parent._cast(_6997.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7001.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7001

            return self._parent._cast(_7001.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7002.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7002

            return self._parent._cast(_7002.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7007.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7007

            return self._parent._cast(_7007.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7008.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7008

            return self._parent._cast(_7008.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7009.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7009

            return self._parent._cast(_7009.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "_7012.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7012

            return self._parent._cast(_7012.ZerolBevelGearLoadCase)

        @property
        def mountable_component_load_case(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
        ) -> "MountableComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "MountableComponentLoadCase._Cast_MountableComponentLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MountableComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2482.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentLoadCase._Cast_MountableComponentLoadCase":
        return self._Cast_MountableComponentLoadCase(self)
