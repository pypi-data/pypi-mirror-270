"""MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3682,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3604,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3661,
        _3665,
        _3668,
        _3671,
        _3672,
        _3673,
        _3680,
        _3685,
        _3686,
        _3689,
        _3693,
        _3696,
        _3699,
        _3704,
        _3707,
        _3710,
        _3715,
        _3719,
        _3723,
        _3726,
        _3729,
        _3732,
        _3733,
        _3735,
        _3739,
        _3742,
        _3743,
        _3744,
        _3745,
        _3746,
        _3749,
        _3753,
        _3756,
        _3761,
        _3762,
        _3765,
        _3768,
        _3769,
        _3771,
        _3772,
        _3773,
        _3776,
        _3777,
        _3778,
        _3779,
        _3780,
        _3783,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed"
)


class MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(
    _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
):
    """MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3682.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3661.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.AGMAGleasonConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bearing_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3665.BearingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3665,
            )

            return self._parent._cast(
                _3665.BearingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3668.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3668,
            )

            return self._parent._cast(
                _3668.BevelDifferentialGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3671.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3671,
            )

            return self._parent._cast(
                _3671.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3672.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3672,
            )

            return self._parent._cast(
                _3672.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3673.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3673,
            )

            return self._parent._cast(
                _3673.BevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3680.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3680,
            )

            return self._parent._cast(
                _3680.ClutchHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3685.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3685,
            )

            return self._parent._cast(
                _3685.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3686.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3686,
            )

            return self._parent._cast(
                _3686.ConceptGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3689,
            )

            return self._parent._cast(
                _3689.ConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connector_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3693.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3693,
            )

            return self._parent._cast(
                _3693.ConnectorCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3696.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3696,
            )

            return self._parent._cast(
                _3696.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3699.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3699,
            )

            return self._parent._cast(
                _3699.CVTPulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3704.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3704,
            )

            return self._parent._cast(
                _3704.CylindricalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3707.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3707,
            )

            return self._parent._cast(
                _3707.CylindricalPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3710.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3710,
            )

            return self._parent._cast(
                _3710.FaceGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.GearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.GearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3719.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3719,
            )

            return self._parent._cast(
                _3719.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3723.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3723,
            )

            return self._parent._cast(
                _3723.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3726.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3726,
            )

            return self._parent._cast(
                _3726.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3729.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3729,
            )

            return self._parent._cast(
                _3729.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3732.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3732,
            )

            return self._parent._cast(
                _3732.MassDiscCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3733.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3733,
            )

            return self._parent._cast(
                _3733.MeasurementComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3735.OilSealCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3735,
            )

            return self._parent._cast(
                _3735.OilSealCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3739.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3739,
            )

            return self._parent._cast(
                _3739.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3742.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3742,
            )

            return self._parent._cast(
                _3742.PlanetCarrierCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def point_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3743.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3743,
            )

            return self._parent._cast(
                _3743.PointLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def power_load_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3744.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3744,
            )

            return self._parent._cast(
                _3744.PowerLoadCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def pulley_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3745.PulleyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3745,
            )

            return self._parent._cast(
                _3745.PulleyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3746.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3746,
            )

            return self._parent._cast(
                _3746.RingPinsCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3749.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3749,
            )

            return self._parent._cast(
                _3749.RollingRingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3753.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3753,
            )

            return self._parent._cast(
                _3753.ShaftHubConnectionCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3756.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3756,
            )

            return self._parent._cast(
                _3756.SpiralBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3761.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3761,
            )

            return self._parent._cast(
                _3761.SpringDamperHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3762.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3762,
            )

            return self._parent._cast(
                _3762.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3765.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3765,
            )

            return self._parent._cast(
                _3765.StraightBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3768.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3768,
            )

            return self._parent._cast(
                _3768.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3769.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3769,
            )

            return self._parent._cast(
                _3769.StraightBevelSunGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3771.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3771,
            )

            return self._parent._cast(
                _3771.SynchroniserHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3772.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3772,
            )

            return self._parent._cast(
                _3772.SynchroniserPartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3773.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3773,
            )

            return self._parent._cast(
                _3773.SynchroniserSleeveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3776.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3776,
            )

            return self._parent._cast(
                _3776.TorqueConverterPumpCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "_3777.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3777,
            )

            return self._parent._cast(
                _3777.TorqueConverterTurbineCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def unbalanced_mass_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3778.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3778,
            )

            return self._parent._cast(
                _3778.UnbalancedMassCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3779.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3779,
            )

            return self._parent._cast(
                _3779.VirtualComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3780.WormGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3780,
            )

            return self._parent._cast(
                _3780.WormGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3783.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3783,
            )

            return self._parent._cast(
                _3783.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.MountableComponentSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3604.MountableComponentSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.MountableComponentSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
