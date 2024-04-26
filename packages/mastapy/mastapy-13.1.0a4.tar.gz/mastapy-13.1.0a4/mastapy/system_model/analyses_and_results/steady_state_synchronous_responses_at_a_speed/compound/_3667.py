"""BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3755,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3537,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3698,
        _3657,
        _3736,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed")


class BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed(
    _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
):
    """BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3755.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3657,
            )

            return self._parent._cast(
                _3657.AbstractAssemblyCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3736.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3736,
            )

            return self._parent._cast(
                _3736.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3698.CVTCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3698,
            )

            return self._parent._cast(
                _3698.CVTCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def belt_drive_compound_steady_state_synchronous_response_at_a_speed(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

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
    ) -> "List[_3537.BeltDriveSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BeltDriveSteadyStateSynchronousResponseAtASpeed]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3537.BeltDriveSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.BeltDriveSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_BeltDriveCompoundSteadyStateSynchronousResponseAtASpeed(self)
