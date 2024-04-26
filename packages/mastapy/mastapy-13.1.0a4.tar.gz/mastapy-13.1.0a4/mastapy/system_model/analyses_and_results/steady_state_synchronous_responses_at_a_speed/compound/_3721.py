"""HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3663,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3590,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3719,
        _3720,
        _3691,
        _3717,
        _3755,
        _3657,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed"
)


class HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
):
    """HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3590.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]

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
    def hypoid_gears_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3719.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.HypoidGearCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3720.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.HypoidGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundSteadyStateSynchronousResponseAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3590.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.HypoidGearSetSteadyStateSynchronousResponseAtASpeed]

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
    def cast_to(
        self: Self,
    ) -> "HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_HypoidGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
