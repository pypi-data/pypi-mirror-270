"""OilSealStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3822
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "OilSealStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3865,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("OilSealStabilityAnalysis",)


Self = TypeVar("Self", bound="OilSealStabilityAnalysis")


class OilSealStabilityAnalysis(_3822.ConnectorStabilityAnalysis):
    """OilSealStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_OilSealStabilityAnalysis")

    class _Cast_OilSealStabilityAnalysis:
        """Special nested class for casting OilSealStabilityAnalysis to subclasses."""

        def __init__(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
            parent: "OilSealStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connector_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3822.ConnectorStabilityAnalysis":
            return self._parent._cast(_3822.ConnectorStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis",
        ) -> "OilSealStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "OilSealStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6953.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "OilSealStabilityAnalysis._Cast_OilSealStabilityAnalysis":
        return self._Cast_OilSealStabilityAnalysis(self)
