"""ConceptCouplingConnectionCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "ConceptCouplingConnectionCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.static_loads import _6865
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6637,
        _6604,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingConnectionCriticalSpeedAnalysis")


class ConceptCouplingConnectionCriticalSpeedAnalysis(
    _6606.CouplingConnectionCriticalSpeedAnalysis
):
    """ConceptCouplingConnectionCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingConnectionCriticalSpeedAnalysis"
    )

    class _Cast_ConceptCouplingConnectionCriticalSpeedAnalysis:
        """Special nested class for casting ConceptCouplingConnectionCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
            parent: "ConceptCouplingConnectionCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_connection_critical_speed_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_6606.CouplingConnectionCriticalSpeedAnalysis":
            return self._parent._cast(_6606.CouplingConnectionCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_6637.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(
                _6637.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_6604.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6604,
            )

            return self._parent._cast(_6604.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_critical_speed_analysis(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
        ) -> "ConceptCouplingConnectionCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis",
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
        instance_to_wrap: "ConceptCouplingConnectionCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2362.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6865.ConceptCouplingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCriticalSpeedAnalysis._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis":
        return self._Cast_ConceptCouplingConnectionCriticalSpeedAnalysis(self)
