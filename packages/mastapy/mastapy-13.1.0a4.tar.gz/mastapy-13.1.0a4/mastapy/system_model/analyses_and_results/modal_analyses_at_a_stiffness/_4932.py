"""DynamicModelAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_MODEL_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "DynamicModelAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7570,
        _7576,
        _7561,
    )
    from mastapy.system_model.analyses_and_results import _2673


__docformat__ = "restructuredtext en"
__all__ = ("DynamicModelAtAStiffness",)


Self = TypeVar("Self", bound="DynamicModelAtAStiffness")


class DynamicModelAtAStiffness(_6355.DynamicAnalysis):
    """DynamicModelAtAStiffness

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_MODEL_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicModelAtAStiffness")

    class _Cast_DynamicModelAtAStiffness:
        """Special nested class for casting DynamicModelAtAStiffness to subclasses."""

        def __init__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
            parent: "DynamicModelAtAStiffness",
        ):
            self._parent = parent

        @property
        def dynamic_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_6355.DynamicAnalysis":
            return self._parent._cast(_6355.DynamicAnalysis)

        @property
        def fe_analysis(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7570.FEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7570

            return self._parent._cast(_7570.FEAnalysis)

        @property
        def static_load_analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7576.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7576

            return self._parent._cast(_7576.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_7561.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.AnalysisCase)

        @property
        def context(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "_2673.Context":
            from mastapy.system_model.analyses_and_results import _2673

            return self._parent._cast(_2673.Context)

        @property
        def dynamic_model_at_a_stiffness(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness",
        ) -> "DynamicModelAtAStiffness":
            return self._parent

        def __getattr__(
            self: "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicModelAtAStiffness.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "DynamicModelAtAStiffness._Cast_DynamicModelAtAStiffness":
        return self._Cast_DynamicModelAtAStiffness(self)
