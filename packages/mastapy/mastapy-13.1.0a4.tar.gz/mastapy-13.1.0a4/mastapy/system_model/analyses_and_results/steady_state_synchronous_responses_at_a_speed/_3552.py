"""ComponentSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3606,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "ComponentSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2462
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3528,
        _3529,
        _3533,
        _3535,
        _3540,
        _3541,
        _3542,
        _3545,
        _3547,
        _3549,
        _3554,
        _3558,
        _3561,
        _3563,
        _3565,
        _3568,
        _3573,
        _3576,
        _3577,
        _3578,
        _3579,
        _3582,
        _3583,
        _3587,
        _3588,
        _3591,
        _3595,
        _3598,
        _3601,
        _3602,
        _3603,
        _3604,
        _3605,
        _3608,
        _3612,
        _3613,
        _3614,
        _3615,
        _3616,
        _3620,
        _3622,
        _3623,
        _3628,
        _3630,
        _3635,
        _3638,
        _3639,
        _3640,
        _3641,
        _3642,
        _3643,
        _3646,
        _3648,
        _3649,
        _3650,
        _3653,
        _3656,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="ComponentSteadyStateSynchronousResponseAtASpeed")


class ComponentSteadyStateSynchronousResponseAtASpeed(
    _3606.PartSteadyStateSynchronousResponseAtASpeed
):
    """ComponentSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_ComponentSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting ComponentSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
            parent: "ComponentSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3606.PartSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(_3606.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3528,
            )

            return self._parent._cast(
                _3528.AbstractShaftOrHousingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_shaft_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3529.AbstractShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3529,
            )

            return self._parent._cast(
                _3529.AbstractShaftSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3533,
            )

            return self._parent._cast(
                _3533.AGMAGleasonConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3535.BearingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3535,
            )

            return self._parent._cast(
                _3535.BearingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.BevelDifferentialGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.BevelDifferentialPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3542.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3542,
            )

            return self._parent._cast(
                _3542.BevelDifferentialSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3545.BevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3545,
            )

            return self._parent._cast(
                _3545.BevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolt_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3547.BoltSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3547,
            )

            return self._parent._cast(_3547.BoltSteadyStateSynchronousResponseAtASpeed)

        @property
        def clutch_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3549.ClutchHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3549,
            )

            return self._parent._cast(
                _3549.ClutchHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3554.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3554,
            )

            return self._parent._cast(
                _3554.ConceptCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3558.ConceptGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3558,
            )

            return self._parent._cast(
                _3558.ConceptGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3561.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3561,
            )

            return self._parent._cast(
                _3561.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3563.ConnectorSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3563,
            )

            return self._parent._cast(
                _3563.ConnectorSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.CouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3568.CVTPulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3568,
            )

            return self._parent._cast(
                _3568.CVTPulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_disc_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.CycloidalDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3573,
            )

            return self._parent._cast(
                _3573.CycloidalDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3576.CylindricalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3576,
            )

            return self._parent._cast(
                _3576.CylindricalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3577.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3577,
            )

            return self._parent._cast(
                _3577.CylindricalPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def datum_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3578.DatumSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3578,
            )

            return self._parent._cast(_3578.DatumSteadyStateSynchronousResponseAtASpeed)

        @property
        def external_cad_model_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3579.ExternalCADModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3579,
            )

            return self._parent._cast(
                _3579.ExternalCADModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3582.FaceGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3582,
            )

            return self._parent._cast(
                _3582.FaceGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def fe_part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.FEPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.FEPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3587.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3587,
            )

            return self._parent._cast(_3587.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def guide_dxf_model_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3588,
            )

            return self._parent._cast(
                _3588.GuideDxfModelSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3591.HypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3591,
            )

            return self._parent._cast(
                _3591.HypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3595,
            )

            return self._parent._cast(
                _3595.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3598.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3598,
            )

            return self._parent._cast(
                _3598.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3601.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3601,
            )

            return self._parent._cast(
                _3601.KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3602.MassDiscSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3602,
            )

            return self._parent._cast(
                _3602.MassDiscSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3603.MeasurementComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3603,
            )

            return self._parent._cast(
                _3603.MeasurementComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3605.OilSealSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3605,
            )

            return self._parent._cast(
                _3605.OilSealSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3608.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3608,
            )

            return self._parent._cast(
                _3608.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3612.PlanetCarrierSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3612,
            )

            return self._parent._cast(
                _3612.PlanetCarrierSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3613.PointLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3613,
            )

            return self._parent._cast(
                _3613.PointLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3614.PowerLoadSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3614,
            )

            return self._parent._cast(
                _3614.PowerLoadSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3615.PulleySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3615,
            )

            return self._parent._cast(
                _3615.PulleySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3616.RingPinsSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3616,
            )

            return self._parent._cast(
                _3616.RingPinsSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3620.RollingRingSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3620,
            )

            return self._parent._cast(
                _3620.RollingRingSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3622.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3622,
            )

            return self._parent._cast(
                _3622.ShaftHubConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3623.ShaftSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3623,
            )

            return self._parent._cast(_3623.ShaftSteadyStateSynchronousResponseAtASpeed)

        @property
        def spiral_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3628.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3628,
            )

            return self._parent._cast(
                _3628.SpiralBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3630.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3630,
            )

            return self._parent._cast(
                _3630.SpringDamperHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3635,
            )

            return self._parent._cast(
                _3635.StraightBevelDiffGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3638.StraightBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3638,
            )

            return self._parent._cast(
                _3638.StraightBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3639.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3639,
            )

            return self._parent._cast(
                _3639.StraightBevelPlanetGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3640.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3640,
            )

            return self._parent._cast(
                _3640.StraightBevelSunGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3641.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3641,
            )

            return self._parent._cast(
                _3641.SynchroniserHalfSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3642.SynchroniserPartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3642,
            )

            return self._parent._cast(
                _3642.SynchroniserPartSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3643.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3643,
            )

            return self._parent._cast(
                _3643.SynchroniserSleeveSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3646.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3646,
            )

            return self._parent._cast(
                _3646.TorqueConverterPumpSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3648.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3648,
            )

            return self._parent._cast(
                _3648.TorqueConverterTurbineSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3649,
            )

            return self._parent._cast(
                _3649.UnbalancedMassSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3650.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3650,
            )

            return self._parent._cast(
                _3650.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3653.WormGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3653,
            )

            return self._parent._cast(
                _3653.WormGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3656.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3656,
            )

            return self._parent._cast(
                _3656.ZerolBevelGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
        ) -> "ComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed",
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
        self: Self,
        instance_to_wrap: "ComponentSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2462.Component":
        """mastapy.system_model.part_model.Component

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
    ) -> "ComponentSteadyStateSynchronousResponseAtASpeed._Cast_ComponentSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_ComponentSteadyStateSynchronousResponseAtASpeed(self)
