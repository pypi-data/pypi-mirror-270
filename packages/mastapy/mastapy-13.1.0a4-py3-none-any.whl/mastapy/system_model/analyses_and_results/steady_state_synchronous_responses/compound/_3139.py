"""AbstractAssemblyCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3218,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "AbstractAssemblyCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3006,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3145,
        _3146,
        _3149,
        _3152,
        _3157,
        _3159,
        _3160,
        _3165,
        _3170,
        _3173,
        _3176,
        _3180,
        _3182,
        _3188,
        _3194,
        _3196,
        _3199,
        _3203,
        _3207,
        _3210,
        _3213,
        _3219,
        _3223,
        _3230,
        _3233,
        _3237,
        _3240,
        _3241,
        _3246,
        _3249,
        _3252,
        _3256,
        _3264,
        _3267,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundSteadyStateSynchronousResponse")


class AbstractAssemblyCompoundSteadyStateSynchronousResponse(
    _3218.PartCompoundSteadyStateSynchronousResponse
):
    """AbstractAssemblyCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting AbstractAssemblyCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
            parent: "AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def part_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3145.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3145,
            )

            return self._parent._cast(
                _3145.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3146.AssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3146,
            )

            return self._parent._cast(
                _3146.AssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.BeltDriveCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.BeltDriveCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3157,
            )

            return self._parent._cast(
                _3157.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bolted_joint_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3159.BoltedJointCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3159,
            )

            return self._parent._cast(
                _3159.BoltedJointCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3160.ClutchCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3160,
            )

            return self._parent._cast(
                _3160.ClutchCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3165.ConceptCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3165,
            )

            return self._parent._cast(
                _3165.ConceptCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3170.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3170,
            )

            return self._parent._cast(
                _3170.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3173.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.CouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3176,
            )

            return self._parent._cast(
                _3176.CouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3180.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(_3180.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def cycloidal_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3182.CycloidalAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.CycloidalAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3188.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3188,
            )

            return self._parent._cast(
                _3188.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3194.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3194,
            )

            return self._parent._cast(
                _3194.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3196.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3196,
            )

            return self._parent._cast(
                _3196.FlexiblePinAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3199.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3199,
            )

            return self._parent._cast(
                _3199.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3203.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3203,
            )

            return self._parent._cast(
                _3203.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3207.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3207,
            )

            return self._parent._cast(
                _3207.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3210.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3210,
            )

            return self._parent._cast(
                _3210.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3213.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3213,
            )

            return self._parent._cast(
                _3213.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3219.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.PartToPartShearCouplingCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3223.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3223,
            )

            return self._parent._cast(
                _3223.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3230.RollingRingAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3230,
            )

            return self._parent._cast(
                _3230.RollingRingAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def root_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3233.RootAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3233,
            )

            return self._parent._cast(
                _3233.RootAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3237,
            )

            return self._parent._cast(
                _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3240.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3240,
            )

            return self._parent._cast(
                _3240.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3241.SpringDamperCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3241,
            )

            return self._parent._cast(
                _3241.SpringDamperCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3246.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3249.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3249,
            )

            return self._parent._cast(
                _3249.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def synchroniser_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3252.SynchroniserCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3252,
            )

            return self._parent._cast(
                _3252.SynchroniserCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3256.TorqueConverterCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3256,
            )

            return self._parent._cast(
                _3256.TorqueConverterCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3264.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3264,
            )

            return self._parent._cast(
                _3264.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "_3267.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3267,
            )

            return self._parent._cast(
                _3267.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
        ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "AbstractAssemblyCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3006.AbstractAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractAssemblySteadyStateSynchronousResponse]

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
    ) -> "List[_3006.AbstractAssemblySteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.AbstractAssemblySteadyStateSynchronousResponse]

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
    ) -> "AbstractAssemblyCompoundSteadyStateSynchronousResponse._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse":
        return self._Cast_AbstractAssemblyCompoundSteadyStateSynchronousResponse(self)
