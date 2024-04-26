"""CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5402
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2356
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis"
)


class CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis(
    _5402.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5402.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            return self._parent._cast(
                _5402.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2356.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6887.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
        return (
            self._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis(
                self
            )
        )
