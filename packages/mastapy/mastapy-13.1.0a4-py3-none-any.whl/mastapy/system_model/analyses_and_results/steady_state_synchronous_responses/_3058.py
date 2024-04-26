"""DynamicModelForSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "DynamicModelForSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7570,
        _7576,
        _7561,
    )
    from mastapy.system_model.analyses_and_results import _2673


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelForSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="DynamicModelForSteadyStateSynchronousResponse")


class DynamicModelForSteadyStateSynchronousResponse(_6355.DynamicAnalysis):
    """DynamicModelForSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_FOR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DynamicModelForSteadyStateSynchronousResponse"
    )

    class _Cast_DynamicModelForSteadyStateSynchronousResponse:
        """Special nested class for casting DynamicModelForSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
            parent: "DynamicModelForSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "_6355.DynamicAnalysis":
            return self._parent._cast(_6355.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "_7570.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "_7576.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7576

            return self._parent._cast(_7576.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "_7561.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.AnalysisCase)

        @property
        def context(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "_2673.Context":
            from mastapy.system_model.analyses_and_results import _2673

            return self._parent._cast(_2673.Context)

        @property
        def dynamic_model_for_steady_state_synchronous_response(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
        ) -> "DynamicModelForSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse",
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
        instance_to_wrap: "DynamicModelForSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelForSteadyStateSynchronousResponse._Cast_DynamicModelForSteadyStateSynchronousResponse":
        return self._Cast_DynamicModelForSteadyStateSynchronousResponse(self)
