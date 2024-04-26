"""SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3398,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3366,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3404,
        _3408,
        _3411,
        _3416,
        _3418,
        _3419,
        _3424,
        _3429,
        _3432,
        _3435,
        _3439,
        _3441,
        _3447,
        _3453,
        _3455,
        _3458,
        _3462,
        _3466,
        _3469,
        _3472,
        _3478,
        _3482,
        _3489,
        _3499,
        _3500,
        _3505,
        _3508,
        _3511,
        _3515,
        _3523,
        _3526,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"
)


class SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
    _3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
):
    """SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3408.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3408,
            )

            return self._parent._cast(
                _3408.BeltDriveCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3411.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3411,
            )

            return self._parent._cast(
                _3411.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3416,
            )

            return self._parent._cast(
                _3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3418.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3418,
            )

            return self._parent._cast(
                _3418.BoltedJointCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def clutch_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3419.ClutchCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3419,
            )

            return self._parent._cast(
                _3419.ClutchCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3424.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3424,
            )

            return self._parent._cast(
                _3424.ConceptCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3429.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3429,
            )

            return self._parent._cast(
                _3429.ConceptGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3435.CouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3435,
            )

            return self._parent._cast(
                _3435.CouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cvt_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3439.CVTCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3439,
            )

            return self._parent._cast(
                _3439.CVTCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3441.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3441,
            )

            return self._parent._cast(
                _3441.CycloidalAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3447.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3447,
            )

            return self._parent._cast(
                _3447.CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3453.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3453,
            )

            return self._parent._cast(
                _3453.FaceGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3462.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3462,
            )

            return self._parent._cast(
                _3462.HypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3466.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3466,
            )

            return self._parent._cast(
                _3466.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3469.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3469,
            )

            return self._parent._cast(
                _3469.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3472.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3472,
            )

            return self._parent._cast(
                _3472.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3478.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3478,
            )

            return self._parent._cast(
                _3478.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3489.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3489,
            )

            return self._parent._cast(
                _3489.RollingRingAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3499.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3499,
            )

            return self._parent._cast(
                _3499.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3500.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3500,
            )

            return self._parent._cast(
                _3500.SpringDamperCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3505.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3505,
            )

            return self._parent._cast(
                _3505.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3508.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3508,
            )

            return self._parent._cast(
                _3508.StraightBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3511.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3511,
            )

            return self._parent._cast(
                _3511.SynchroniserCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3515.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3515,
            )

            return self._parent._cast(
                _3515.TorqueConverterCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3523.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3523,
            )

            return self._parent._cast(
                _3523.WormGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3526.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3526,
            )

            return self._parent._cast(
                _3526.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
