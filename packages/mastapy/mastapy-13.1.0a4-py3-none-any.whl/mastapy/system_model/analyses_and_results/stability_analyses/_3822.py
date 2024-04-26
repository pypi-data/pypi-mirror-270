"""ConnectorStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectorStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3794,
        _3866,
        _3883,
        _3811,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectorStabilityAnalysis")


class ConnectorStabilityAnalysis(_3865.MountableComponentStabilityAnalysis):
    """ConnectorStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectorStabilityAnalysis")

    class _Cast_ConnectorStabilityAnalysis:
        """Special nested class for casting ConnectorStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            parent: "ConnectorStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3865.MountableComponentStabilityAnalysis":
            return self._parent._cast(_3865.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3811.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3811,
            )

            return self._parent._cast(_3811.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3794.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3794,
            )

            return self._parent._cast(_3794.BearingStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3866.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.OilSealStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "_3883.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.ShaftHubConnectionStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
        ) -> "ConnectorStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectorStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.Connector":
        """mastapy.system_model.part_model.Connector

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectorStabilityAnalysis._Cast_ConnectorStabilityAnalysis":
        return self._Cast_ConnectorStabilityAnalysis(self)
