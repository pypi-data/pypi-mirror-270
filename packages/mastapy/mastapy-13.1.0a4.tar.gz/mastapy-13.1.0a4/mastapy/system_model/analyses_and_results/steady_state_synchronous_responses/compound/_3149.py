"""BeltDriveCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3237,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "BeltDriveCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3016,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3180,
        _3139,
        _3218,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BeltDriveCompoundSteadyStateSynchronousResponse")


class BeltDriveCompoundSteadyStateSynchronousResponse(
    _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
):
    """BeltDriveCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_BeltDriveCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting BeltDriveCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
            parent: "BeltDriveCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3237.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3139,
            )

            return self._parent._cast(
                _3139.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_3218.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3218,
            )

            return self._parent._cast(_3218.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_steady_state_synchronous_response(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "_3180.CVTCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3180,
            )

            return self._parent._cast(_3180.CVTCompoundSteadyStateSynchronousResponse)

        @property
        def belt_drive_compound_steady_state_synchronous_response(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
        ) -> "BeltDriveCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BeltDriveCompoundSteadyStateSynchronousResponse.TYPE",
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
    ) -> "List[_3016.BeltDriveSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BeltDriveSteadyStateSynchronousResponse]

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
    ) -> "List[_3016.BeltDriveSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BeltDriveSteadyStateSynchronousResponse]

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
    ) -> "BeltDriveCompoundSteadyStateSynchronousResponse._Cast_BeltDriveCompoundSteadyStateSynchronousResponse":
        return self._Cast_BeltDriveCompoundSteadyStateSynchronousResponse(self)
