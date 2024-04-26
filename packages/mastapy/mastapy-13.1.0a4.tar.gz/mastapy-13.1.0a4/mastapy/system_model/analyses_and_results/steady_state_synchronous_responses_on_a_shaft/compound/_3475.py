"""MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3423,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3345,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3402,
        _3406,
        _3409,
        _3412,
        _3413,
        _3414,
        _3421,
        _3426,
        _3427,
        _3430,
        _3434,
        _3437,
        _3440,
        _3445,
        _3448,
        _3451,
        _3456,
        _3460,
        _3464,
        _3467,
        _3470,
        _3473,
        _3474,
        _3476,
        _3480,
        _3483,
        _3484,
        _3485,
        _3486,
        _3487,
        _3490,
        _3494,
        _3497,
        _3502,
        _3503,
        _3506,
        _3509,
        _3510,
        _3512,
        _3513,
        _3514,
        _3517,
        _3518,
        _3519,
        _3520,
        _3521,
        _3524,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft"
)


class MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft(
    _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3402.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3406.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3409.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3409,
            )

            return self._parent._cast(
                _3409.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3421.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3426.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3427.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3430.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3434.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3440.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3445.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3448.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3448,
            )

            return self._parent._cast(
                _3448.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3451.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3473.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3474.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3476.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3480.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3480,
            )

            return self._parent._cast(
                _3480.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3483.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3484.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3485.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3486.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3487.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3490.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3503.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3503,
            )

            return self._parent._cast(
                _3503.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3510,
            )

            return self._parent._cast(
                _3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3512,
            )

            return self._parent._cast(
                _3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3513,
            )

            return self._parent._cast(
                _3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3517.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3517,
            )

            return self._parent._cast(
                _3517.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3518.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3518,
            )

            return self._parent._cast(
                _3518.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3519.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3519,
            )

            return self._parent._cast(
                _3519.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3520.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3520,
            )

            return self._parent._cast(
                _3520.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3521.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3521,
            )

            return self._parent._cast(
                _3521.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3524,
            )

            return self._parent._cast(
                _3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3345.MountableComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.MountableComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3345.MountableComponentSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.MountableComponentSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
