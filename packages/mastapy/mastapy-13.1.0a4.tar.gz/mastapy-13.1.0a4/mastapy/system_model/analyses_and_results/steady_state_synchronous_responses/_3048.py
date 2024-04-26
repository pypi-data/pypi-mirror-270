"""CVTSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3016,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CVTSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3105,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CVTSteadyStateSynchronousResponse")


class CVTSteadyStateSynchronousResponse(_3016.BeltDriveSteadyStateSynchronousResponse):
    """CVTSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CVT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTSteadyStateSynchronousResponse")

    class _Cast_CVTSteadyStateSynchronousResponse:
        """Special nested class for casting CVTSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
            parent: "CVTSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def belt_drive_steady_state_synchronous_response(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_3016.BeltDriveSteadyStateSynchronousResponse":
            return self._parent._cast(_3016.BeltDriveSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_steady_state_synchronous_response(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
        ) -> "CVTSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CVTSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTSteadyStateSynchronousResponse._Cast_CVTSteadyStateSynchronousResponse":
        return self._Cast_CVTSteadyStateSynchronousResponse(self)
