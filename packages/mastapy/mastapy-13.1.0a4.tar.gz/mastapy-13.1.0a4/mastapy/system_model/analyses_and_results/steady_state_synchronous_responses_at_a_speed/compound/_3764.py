"""StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3675,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2564
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3634,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3762,
        _3763,
        _3663,
        _3691,
        _3717,
        _3755,
        _3657,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
)


class StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
    _3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
):
    """StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3675.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3663,
            )

            return self._parent._cast(
                _3663.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3691,
            )

            return self._parent._cast(
                _3691.ConicalGearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3717,
            )

            return self._parent._cast(
                _3717.GearSetCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3755,
            )

            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response_at_a_speed(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_3634.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]

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
    def straight_bevel_diff_gears_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3762.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffGearsCompoundSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3763.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3634.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
