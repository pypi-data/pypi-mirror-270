"""PartCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7572
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "PartCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3347,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3398,
        _3399,
        _3400,
        _3402,
        _3404,
        _3405,
        _3406,
        _3408,
        _3409,
        _3411,
        _3412,
        _3413,
        _3414,
        _3416,
        _3417,
        _3418,
        _3419,
        _3421,
        _3423,
        _3424,
        _3426,
        _3427,
        _3429,
        _3430,
        _3432,
        _3434,
        _3435,
        _3437,
        _3439,
        _3440,
        _3441,
        _3443,
        _3445,
        _3447,
        _3448,
        _3449,
        _3450,
        _3451,
        _3453,
        _3454,
        _3455,
        _3456,
        _3458,
        _3459,
        _3460,
        _3462,
        _3464,
        _3466,
        _3467,
        _3469,
        _3470,
        _3472,
        _3473,
        _3474,
        _3475,
        _3476,
        _3478,
        _3480,
        _3482,
        _3483,
        _3484,
        _3485,
        _3486,
        _3487,
        _3489,
        _3490,
        _3492,
        _3493,
        _3494,
        _3496,
        _3497,
        _3499,
        _3500,
        _3502,
        _3503,
        _3505,
        _3506,
        _3508,
        _3509,
        _3510,
        _3511,
        _3512,
        _3513,
        _3514,
        _3515,
        _3517,
        _3518,
        _3519,
        _3520,
        _3521,
        _3523,
        _3524,
        _3526,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PartCompoundSteadyStateSynchronousResponseOnAShaft")


class PartCompoundSteadyStateSynchronousResponseOnAShaft(_7572.PartCompoundAnalysis):
    """PartCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PartCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3399.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3399,
            )

            return self._parent._cast(
                _3399.AbstractShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_shaft_or_housing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> (
            "_3400.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft"
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3400,
            )

            return self._parent._cast(
                _3400.AbstractShaftOrHousingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3405.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3405,
            )

            return self._parent._cast(
                _3405.AssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3406.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3406,
            )

            return self._parent._cast(
                _3406.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3411.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3412,
            )

            return self._parent._cast(
                _3412.BevelDifferentialPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3413,
            )

            return self._parent._cast(
                _3413.BevelDifferentialSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3414,
            )

            return self._parent._cast(
                _3414.BevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3416,
            )

            return self._parent._cast(
                _3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3417.BoltCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3417,
            )

            return self._parent._cast(
                _3417.BoltCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3419.ClutchCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3421.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3421,
            )

            return self._parent._cast(
                _3421.ClutchHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3423,
            )

            return self._parent._cast(
                _3423.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3424.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3426.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3426,
            )

            return self._parent._cast(
                _3426.ConceptCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3427.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3427,
            )

            return self._parent._cast(
                _3427.ConceptGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3429.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3430.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3430,
            )

            return self._parent._cast(
                _3430.ConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3434.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3434,
            )

            return self._parent._cast(
                _3434.ConnectorCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3435.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3437,
            )

            return self._parent._cast(
                _3437.CouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3439.CVTCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3440.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3440,
            )

            return self._parent._cast(
                _3440.CVTPulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3443.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3443,
            )

            return self._parent._cast(
                _3443.CycloidalDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3445.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3445,
            )

            return self._parent._cast(
                _3445.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3447.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3449.DatumCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3449,
            )

            return self._parent._cast(
                _3449.DatumCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def external_cad_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3450.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3450,
            )

            return self._parent._cast(
                _3450.ExternalCADModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3451.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3451,
            )

            return self._parent._cast(
                _3451.FaceGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3453.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3453,
            )

            return self._parent._cast(
                _3453.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def fe_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.FEPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3454,
            )

            return self._parent._cast(
                _3454.FEPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.GearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.GearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def guide_dxf_model_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3459.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3459,
            )

            return self._parent._cast(
                _3459.GuideDxfModelCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3460,
            )

            return self._parent._cast(
                _3460.HypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3464,
            )

            return self._parent._cast(
                _3464.KlingelnbergCycloPalloidConicalGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3466.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3467,
            )

            return self._parent._cast(
                _3467.KlingelnbergCycloPalloidHypoidGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3470,
            )

            return self._parent._cast(
                _3470.KlingelnbergCycloPalloidSpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3472.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mass_disc_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3473.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.MassDiscCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def measurement_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3474.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3474,
            )

            return self._parent._cast(
                _3474.MeasurementComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3475,
            )

            return self._parent._cast(
                _3475.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3476.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3476,
            )

            return self._parent._cast(
                _3476.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3478.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3480.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3480,
            )

            return self._parent._cast(
                _3480.PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planet_carrier_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3483.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3483,
            )

            return self._parent._cast(
                _3483.PlanetCarrierCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def point_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3484.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3484,
            )

            return self._parent._cast(
                _3484.PointLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def power_load_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3485.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3485,
            )

            return self._parent._cast(
                _3485.PowerLoadCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def pulley_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3486.PulleyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3486,
            )

            return self._parent._cast(
                _3486.PulleyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def ring_pins_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3487.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3487,
            )

            return self._parent._cast(
                _3487.RingPinsCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3489.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3490.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3490,
            )

            return self._parent._cast(
                _3490.RollingRingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3492.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3492,
            )

            return self._parent._cast(
                _3492.RootAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3493.ShaftCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3493,
            )

            return self._parent._cast(
                _3493.ShaftCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3494.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3494,
            )

            return self._parent._cast(
                _3494.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3497,
            )

            return self._parent._cast(
                _3497.SpiralBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3499.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3500.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3502.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3502,
            )

            return self._parent._cast(
                _3502.SpringDamperHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3505.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3506,
            )

            return self._parent._cast(
                _3506.StraightBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3508.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3508,
            )

            return self._parent._cast(
                _3508.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_planet_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3509,
            )

            return self._parent._cast(
                _3509.StraightBevelPlanetGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_sun_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3510,
            )

            return self._parent._cast(
                _3510.StraightBevelSunGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3511.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3511,
            )

            return self._parent._cast(
                _3511.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_half_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3512,
            )

            return self._parent._cast(
                _3512.SynchroniserHalfCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3513,
            )

            return self._parent._cast(
                _3513.SynchroniserPartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_sleeve_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3514,
            )

            return self._parent._cast(
                _3514.SynchroniserSleeveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3515.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3515,
            )

            return self._parent._cast(
                _3515.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_pump_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3517.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3517,
            )

            return self._parent._cast(
                _3517.TorqueConverterPumpCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_turbine_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3519.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3519,
            )

            return self._parent._cast(
                _3519.UnbalancedMassCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def virtual_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3520.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3520,
            )

            return self._parent._cast(
                _3520.VirtualComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3521.WormGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3521,
            )

            return self._parent._cast(
                _3521.WormGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3523.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3524,
            )

            return self._parent._cast(
                _3524.ZerolBevelGearCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3526.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3526,
            )

            return self._parent._cast(
                _3526.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "PartCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PartCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3347.PartSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3347.PartSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.PartSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "PartCompoundSteadyStateSynchronousResponseOnAShaft._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PartCompoundSteadyStateSynchronousResponseOnAShaft(self)
