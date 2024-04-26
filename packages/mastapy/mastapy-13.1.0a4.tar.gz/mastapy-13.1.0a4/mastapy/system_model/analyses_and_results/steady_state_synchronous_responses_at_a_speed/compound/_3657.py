"""AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3736,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3527,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3663,
        _3664,
        _3667,
        _3670,
        _3675,
        _3677,
        _3678,
        _3683,
        _3688,
        _3691,
        _3694,
        _3698,
        _3700,
        _3706,
        _3712,
        _3714,
        _3717,
        _3721,
        _3725,
        _3728,
        _3731,
        _3737,
        _3741,
        _3748,
        _3751,
        _3755,
        _3758,
        _3759,
        _3764,
        _3767,
        _3770,
        _3774,
        _3782,
        _3785,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed"
)


class AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(
    _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
):
    """AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3664.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3664,
            )

            return self._parent._cast(
                _3664.AssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3667.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3667,
            )

            return self._parent._cast(
                _3667.BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3670.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3670,
            )

            return self._parent._cast(
                _3670.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3675,
            )

            return self._parent._cast(
                _3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3677.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3677,
            )

            return self._parent._cast(
                _3677.BoltedJointCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def clutch_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3678.ClutchCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3678,
            )

            return self._parent._cast(
                _3678.ClutchCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3683.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3683,
            )

            return self._parent._cast(
                _3683.ConceptCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3688.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3688,
            )

            return self._parent._cast(
                _3688.ConceptGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3694.CouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3694,
            )

            return self._parent._cast(
                _3694.CouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3698.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3700.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3700,
            )

            return self._parent._cast(
                _3700.CycloidalAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3706.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3706,
            )

            return self._parent._cast(
                _3706.CylindricalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3712.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3712,
            )

            return self._parent._cast(
                _3712.FaceGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3714.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3714,
            )

            return self._parent._cast(
                _3714.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3721.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3721,
            )

            return self._parent._cast(
                _3721.HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3725.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3725,
            )

            return self._parent._cast(
                _3725.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3728.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3728,
            )

            return self._parent._cast(
                _3728.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3731.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3731,
            )

            return self._parent._cast(
                _3731.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3737.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3737,
            )

            return self._parent._cast(
                _3737.PartToPartShearCouplingCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3741.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3741,
            )

            return self._parent._cast(
                _3741.PlanetaryGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3748.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3748,
            )

            return self._parent._cast(
                _3748.RollingRingAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3751.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3751,
            )

            return self._parent._cast(
                _3751.RootAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3758.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3758,
            )

            return self._parent._cast(
                _3758.SpiralBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3759.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3759,
            )

            return self._parent._cast(
                _3759.SpringDamperCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3764.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3764,
            )

            return self._parent._cast(
                _3764.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3767.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3767,
            )

            return self._parent._cast(
                _3767.StraightBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3770.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3770,
            )

            return self._parent._cast(
                _3770.SynchroniserCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3774.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3774,
            )

            return self._parent._cast(
                _3774.TorqueConverterCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3782.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3782,
            )

            return self._parent._cast(
                _3782.WormGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3785.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3785,
            )

            return self._parent._cast(
                _3785.ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AbstractAssemblySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "List[_3527.AbstractAssemblySteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.AbstractAssemblySteadyStateSynchronousResponseAtASpeed]

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
    ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
