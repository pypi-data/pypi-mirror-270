"""MountableComponentStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3811
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "MountableComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2482
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3792,
        _3794,
        _3799,
        _3800,
        _3801,
        _3804,
        _3808,
        _3813,
        _3817,
        _3820,
        _3822,
        _3824,
        _3828,
        _3836,
        _3837,
        _3843,
        _3848,
        _3852,
        _3856,
        _3859,
        _3862,
        _3863,
        _3864,
        _3866,
        _3869,
        _3873,
        _3874,
        _3875,
        _3876,
        _3877,
        _3881,
        _3883,
        _3889,
        _3891,
        _3898,
        _3901,
        _3902,
        _3903,
        _3904,
        _3905,
        _3906,
        _3909,
        _3911,
        _3912,
        _3913,
        _3916,
        _3919,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="MountableComponentStabilityAnalysis")


class MountableComponentStabilityAnalysis(_3811.ComponentStabilityAnalysis):
    """MountableComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentStabilityAnalysis")

    class _Cast_MountableComponentStabilityAnalysis:
        """Special nested class for casting MountableComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
            parent: "MountableComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3792.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3794.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.BearingStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3799.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3800.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(
                _3800.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3801.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3804.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3804,
            )

            return self._parent._cast(_3804.BevelGearStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3808.ClutchHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3813.ConceptCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3813,
            )

            return self._parent._cast(_3813.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3817.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3820.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3820,
            )

            return self._parent._cast(_3820.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3822.ConnectorStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3824.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3824,
            )

            return self._parent._cast(_3824.CouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3828.CVTPulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.CVTPulleyStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3836.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3836,
            )

            return self._parent._cast(_3836.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3837.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3837,
            )

            return self._parent._cast(_3837.CylindricalPlanetGearStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3843.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.FaceGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3848.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(_3848.GearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3852.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(
                _3856.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3859,
            )

            return self._parent._cast(
                _3859.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(
                _3862.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3863.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3864.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3864,
            )

            return self._parent._cast(_3864.MeasurementComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3866.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3869.PartToPartShearCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3869,
            )

            return self._parent._cast(
                _3869.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def planet_carrier_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3873.PlanetCarrierStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3873,
            )

            return self._parent._cast(_3873.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3874.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3874,
            )

            return self._parent._cast(_3874.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3875.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3876.PulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3876,
            )

            return self._parent._cast(_3876.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3877.RingPinsStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3881.RollingRingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3883.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.ShaftHubConnectionStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3889.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3889,
            )

            return self._parent._cast(_3889.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3891.SpringDamperHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3898.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3901.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3901,
            )

            return self._parent._cast(_3901.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3902.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3902,
            )

            return self._parent._cast(_3902.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3903.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3903,
            )

            return self._parent._cast(_3903.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3904.SynchroniserHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3904,
            )

            return self._parent._cast(_3904.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3905.SynchroniserPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3905,
            )

            return self._parent._cast(_3905.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3906.SynchroniserSleeveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3906,
            )

            return self._parent._cast(_3906.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3909.TorqueConverterPumpStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3909,
            )

            return self._parent._cast(_3909.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3911.TorqueConverterTurbineStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3911,
            )

            return self._parent._cast(_3911.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3912.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3912,
            )

            return self._parent._cast(_3912.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3913.VirtualComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3913,
            )

            return self._parent._cast(_3913.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3916.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3916,
            )

            return self._parent._cast(_3916.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "_3919.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3919,
            )

            return self._parent._cast(_3919.ZerolBevelGearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
        ) -> "MountableComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "MountableComponentStabilityAnalysis.TYPE"
    ):
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
    ) -> (
        "MountableComponentStabilityAnalysis._Cast_MountableComponentStabilityAnalysis"
    ):
        return self._Cast_MountableComponentStabilityAnalysis(self)
