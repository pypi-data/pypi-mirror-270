"""MountableComponentCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3945
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "MountableComponentCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3865
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3924,
        _3928,
        _3931,
        _3934,
        _3935,
        _3936,
        _3943,
        _3948,
        _3949,
        _3952,
        _3956,
        _3959,
        _3962,
        _3967,
        _3970,
        _3973,
        _3978,
        _3982,
        _3986,
        _3989,
        _3992,
        _3995,
        _3996,
        _3998,
        _4002,
        _4005,
        _4006,
        _4007,
        _4008,
        _4009,
        _4012,
        _4016,
        _4019,
        _4024,
        _4025,
        _4028,
        _4031,
        _4032,
        _4034,
        _4035,
        _4036,
        _4039,
        _4040,
        _4041,
        _4042,
        _4043,
        _4046,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundStabilityAnalysis")


class MountableComponentCompoundStabilityAnalysis(
    _3945.ComponentCompoundStabilityAnalysis
):
    """MountableComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundStabilityAnalysis"
    )

    class _Cast_MountableComponentCompoundStabilityAnalysis:
        """Special nested class for casting MountableComponentCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
            parent: "MountableComponentCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3924.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def bearing_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3928.BearingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3928,
            )

            return self._parent._cast(_3928.BearingCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3931.BevelDifferentialGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(
                _3931.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3934.BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(
                _3934.BevelDifferentialPlanetGearCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3935.BevelDifferentialSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3935,
            )

            return self._parent._cast(
                _3935.BevelDifferentialSunGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3936,
            )

            return self._parent._cast(_3936.BevelGearCompoundStabilityAnalysis)

        @property
        def clutch_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3943.ClutchHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(_3943.ClutchHalfCompoundStabilityAnalysis)

        @property
        def concept_coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3948.ConceptCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3948,
            )

            return self._parent._cast(
                _3948.ConceptCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def concept_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3949.ConceptGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3949,
            )

            return self._parent._cast(_3949.ConceptGearCompoundStabilityAnalysis)

        @property
        def conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.ConicalGearCompoundStabilityAnalysis)

        @property
        def connector_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3956.ConnectorCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3956,
            )

            return self._parent._cast(_3956.ConnectorCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3959.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.CouplingHalfCompoundStabilityAnalysis)

        @property
        def cvt_pulley_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3962.CVTPulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3962,
            )

            return self._parent._cast(_3962.CVTPulleyCompoundStabilityAnalysis)

        @property
        def cylindrical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3967.CylindricalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3967,
            )

            return self._parent._cast(_3967.CylindricalGearCompoundStabilityAnalysis)

        @property
        def cylindrical_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3970.CylindricalPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3970,
            )

            return self._parent._cast(
                _3970.CylindricalPlanetGearCompoundStabilityAnalysis
            )

        @property
        def face_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3973.FaceGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3973,
            )

            return self._parent._cast(_3973.FaceGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3978.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearCompoundStabilityAnalysis)

        @property
        def hypoid_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3982.HypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3982,
            )

            return self._parent._cast(_3982.HypoidGearCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3986.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3986,
            )

            return self._parent._cast(
                _3986.KlingelnbergCycloPalloidConicalGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3989.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3989,
            )

            return self._parent._cast(
                _3989.KlingelnbergCycloPalloidHypoidGearCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3992.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3992,
            )

            return self._parent._cast(
                _3992.KlingelnbergCycloPalloidSpiralBevelGearCompoundStabilityAnalysis
            )

        @property
        def mass_disc_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3995.MassDiscCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3995,
            )

            return self._parent._cast(_3995.MassDiscCompoundStabilityAnalysis)

        @property
        def measurement_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3996.MeasurementComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3996,
            )

            return self._parent._cast(
                _3996.MeasurementComponentCompoundStabilityAnalysis
            )

        @property
        def oil_seal_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_3998.OilSealCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3998,
            )

            return self._parent._cast(_3998.OilSealCompoundStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4002,
            )

            return self._parent._cast(
                _4002.PartToPartShearCouplingHalfCompoundStabilityAnalysis
            )

        @property
        def planet_carrier_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4005.PlanetCarrierCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4005,
            )

            return self._parent._cast(_4005.PlanetCarrierCompoundStabilityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4006.PointLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4006,
            )

            return self._parent._cast(_4006.PointLoadCompoundStabilityAnalysis)

        @property
        def power_load_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4007.PowerLoadCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4007,
            )

            return self._parent._cast(_4007.PowerLoadCompoundStabilityAnalysis)

        @property
        def pulley_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4008.PulleyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4008,
            )

            return self._parent._cast(_4008.PulleyCompoundStabilityAnalysis)

        @property
        def ring_pins_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4009.RingPinsCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4009,
            )

            return self._parent._cast(_4009.RingPinsCompoundStabilityAnalysis)

        @property
        def rolling_ring_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4012.RollingRingCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4012,
            )

            return self._parent._cast(_4012.RollingRingCompoundStabilityAnalysis)

        @property
        def shaft_hub_connection_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4016.ShaftHubConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4016,
            )

            return self._parent._cast(_4016.ShaftHubConnectionCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4019.SpiralBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4019,
            )

            return self._parent._cast(_4019.SpiralBevelGearCompoundStabilityAnalysis)

        @property
        def spring_damper_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4024.SpringDamperHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4024,
            )

            return self._parent._cast(_4024.SpringDamperHalfCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4025.StraightBevelDiffGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4025,
            )

            return self._parent._cast(
                _4025.StraightBevelDiffGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4028.StraightBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4028,
            )

            return self._parent._cast(_4028.StraightBevelGearCompoundStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4031.StraightBevelPlanetGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4031,
            )

            return self._parent._cast(
                _4031.StraightBevelPlanetGearCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4032.StraightBevelSunGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4032,
            )

            return self._parent._cast(
                _4032.StraightBevelSunGearCompoundStabilityAnalysis
            )

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4034.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4034,
            )

            return self._parent._cast(_4034.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4035.SynchroniserPartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4035,
            )

            return self._parent._cast(_4035.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4036.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4036,
            )

            return self._parent._cast(_4036.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def torque_converter_pump_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4039.TorqueConverterPumpCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4039,
            )

            return self._parent._cast(
                _4039.TorqueConverterPumpCompoundStabilityAnalysis
            )

        @property
        def torque_converter_turbine_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4040.TorqueConverterTurbineCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4040,
            )

            return self._parent._cast(
                _4040.TorqueConverterTurbineCompoundStabilityAnalysis
            )

        @property
        def unbalanced_mass_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4041.UnbalancedMassCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4041,
            )

            return self._parent._cast(_4041.UnbalancedMassCompoundStabilityAnalysis)

        @property
        def virtual_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4042.VirtualComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4042,
            )

            return self._parent._cast(_4042.VirtualComponentCompoundStabilityAnalysis)

        @property
        def worm_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4043.WormGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4043,
            )

            return self._parent._cast(_4043.WormGearCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "_4046.ZerolBevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4046,
            )

            return self._parent._cast(_4046.ZerolBevelGearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
        ) -> "MountableComponentCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3865.MountableComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MountableComponentStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3865.MountableComponentStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.MountableComponentStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentCompoundStabilityAnalysis._Cast_MountableComponentCompoundStabilityAnalysis":
        return self._Cast_MountableComponentCompoundStabilityAnalysis(self)
