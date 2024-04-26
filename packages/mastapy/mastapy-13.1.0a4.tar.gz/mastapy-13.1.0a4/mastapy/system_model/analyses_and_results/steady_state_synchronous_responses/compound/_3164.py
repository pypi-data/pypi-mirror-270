"""ComponentCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3218,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ComponentCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3031,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3140,
        _3141,
        _3143,
        _3147,
        _3150,
        _3153,
        _3154,
        _3155,
        _3158,
        _3162,
        _3167,
        _3168,
        _3171,
        _3175,
        _3178,
        _3181,
        _3184,
        _3186,
        _3189,
        _3190,
        _3191,
        _3192,
        _3195,
        _3197,
        _3200,
        _3201,
        _3205,
        _3208,
        _3211,
        _3214,
        _3215,
        _3216,
        _3217,
        _3221,
        _3224,
        _3225,
        _3226,
        _3227,
        _3228,
        _3231,
        _3234,
        _3235,
        _3238,
        _3243,
        _3244,
        _3247,
        _3250,
        _3251,
        _3253,
        _3254,
        _3255,
        _3258,
        _3259,
        _3260,
        _3261,
        _3262,
        _3265,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ComponentCompoundSteadyStateSynchronousResponse")


class ComponentCompoundSteadyStateSynchronousResponse(
    _3218.PartCompoundSteadyStateSynchronousResponse
):
    """ComponentCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_ComponentCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ComponentCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
            parent: "ComponentCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3140.AbstractShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3140,
            )

            return self._parent._cast(
                _3140.AbstractShaftCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3141.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3141,
            )

            return self._parent._cast(
                _3141.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bearing_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3147.BearingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3147,
            )

            return self._parent._cast(
                _3147.BearingCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3150.BevelDifferentialGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3150,
            )

            return self._parent._cast(
                _3150.BevelDifferentialGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3154,
            )

            return self._parent._cast(
                _3154.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3155.BevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3155,
            )

            return self._parent._cast(
                _3155.BevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolt_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3158.BoltCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3158,
            )

            return self._parent._cast(_3158.BoltCompoundSteadyStateSynchronousResponse)

        @property
        def clutch_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3162.ClutchHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3162,
            )

            return self._parent._cast(
                _3162.ClutchHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3167.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(
                _3167.ConceptCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3168.ConceptGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3168,
            )

            return self._parent._cast(
                _3168.ConceptGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3171.ConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3171,
            )

            return self._parent._cast(
                _3171.ConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3175.ConnectorCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3175,
            )

            return self._parent._cast(
                _3175.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.CouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3181.CVTPulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3181,
            )

            return self._parent._cast(
                _3181.CVTPulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3184.CycloidalDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3184,
            )

            return self._parent._cast(
                _3184.CycloidalDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3186.CylindricalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.CylindricalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.CylindricalPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def datum_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3190.DatumCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3190,
            )

            return self._parent._cast(_3190.DatumCompoundSteadyStateSynchronousResponse)

        @property
        def external_cad_model_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3191.ExternalCADModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3191,
            )

            return self._parent._cast(
                _3191.ExternalCADModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3192.FaceGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.FaceGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def fe_part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.FEPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.FEPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.GearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.GearCompoundSteadyStateSynchronousResponse)

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3200.GuideDxfModelCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3200,
            )

            return self._parent._cast(
                _3200.GuideDxfModelCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3201.HypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3201,
            )

            return self._parent._cast(
                _3201.HypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3205.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3205,
            )

            return self._parent._cast(
                _3205.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3208.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3208,
            )

            return self._parent._cast(
                _3208.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3211.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3211,
            )

            return self._parent._cast(
                _3211.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3214.MassDiscCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3214,
            )

            return self._parent._cast(
                _3214.MassDiscCompoundSteadyStateSynchronousResponse
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3215.MeasurementComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3215,
            )

            return self._parent._cast(
                _3215.MeasurementComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3217.OilSealCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3217,
            )

            return self._parent._cast(
                _3217.OilSealCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3221.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3221,
            )

            return self._parent._cast(
                _3221.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3224.PlanetCarrierCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3224,
            )

            return self._parent._cast(
                _3224.PlanetCarrierCompoundSteadyStateSynchronousResponse
            )

        @property
        def point_load_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.PointLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.PointLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def power_load_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3226.PowerLoadCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3226,
            )

            return self._parent._cast(
                _3226.PowerLoadCompoundSteadyStateSynchronousResponse
            )

        @property
        def pulley_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3227.PulleyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3227,
            )

            return self._parent._cast(
                _3227.PulleyCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3228.RingPinsCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.RingPinsCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3231.RollingRingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3231,
            )

            return self._parent._cast(
                _3231.RollingRingCompoundSteadyStateSynchronousResponse
            )

        @property
        def shaft_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3234.ShaftCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3234,
            )

            return self._parent._cast(_3234.ShaftCompoundSteadyStateSynchronousResponse)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3235.ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3235,
            )

            return self._parent._cast(
                _3235.ShaftHubConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3238.SpiralBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3238,
            )

            return self._parent._cast(
                _3238.SpiralBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3243.SpringDamperHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.SpringDamperHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3244.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3244,
            )

            return self._parent._cast(
                _3244.StraightBevelDiffGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3247.StraightBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3247,
            )

            return self._parent._cast(
                _3247.StraightBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3250.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3250,
            )

            return self._parent._cast(
                _3250.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3251.StraightBevelSunGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3251,
            )

            return self._parent._cast(
                _3251.StraightBevelSunGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3253.SynchroniserHalfCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3253,
            )

            return self._parent._cast(
                _3253.SynchroniserHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3254.SynchroniserPartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3254,
            )

            return self._parent._cast(
                _3254.SynchroniserPartCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3255.SynchroniserSleeveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3255,
            )

            return self._parent._cast(
                _3255.SynchroniserSleeveCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3258.TorqueConverterPumpCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3258,
            )

            return self._parent._cast(
                _3258.TorqueConverterPumpCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3259.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3259,
            )

            return self._parent._cast(
                _3259.TorqueConverterTurbineCompoundSteadyStateSynchronousResponse
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3260.UnbalancedMassCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3260,
            )

            return self._parent._cast(
                _3260.UnbalancedMassCompoundSteadyStateSynchronousResponse
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3261.VirtualComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3261,
            )

            return self._parent._cast(
                _3261.VirtualComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3262.WormGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3262,
            )

            return self._parent._cast(
                _3262.WormGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "_3265.ZerolBevelGearCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3265,
            )

            return self._parent._cast(
                _3265.ZerolBevelGearCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
        ) -> "ComponentCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ComponentCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3031.ComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ComponentSteadyStateSynchronousResponse]

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
    ) -> "List[_3031.ComponentSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ComponentSteadyStateSynchronousResponse]

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
    ) -> "ComponentCompoundSteadyStateSynchronousResponse._Cast_ComponentCompoundSteadyStateSynchronousResponse":
        return self._Cast_ComponentCompoundSteadyStateSynchronousResponse(self)
