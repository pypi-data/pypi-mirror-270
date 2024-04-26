"""SynchroniserSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3105,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SynchroniserSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6995
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserSteadyStateSynchronousResponse")


class SynchroniserSteadyStateSynchronousResponse(
    _3105.SpecialisedAssemblySteadyStateSynchronousResponse
):
    """SynchroniserSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSteadyStateSynchronousResponse"
    )

    class _Cast_SynchroniserSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
            parent: "SynchroniserSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_steady_state_synchronous_response(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
        ) -> "SynchroniserSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "SynchroniserSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2625.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6995.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSteadyStateSynchronousResponse._Cast_SynchroniserSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserSteadyStateSynchronousResponse(self)
