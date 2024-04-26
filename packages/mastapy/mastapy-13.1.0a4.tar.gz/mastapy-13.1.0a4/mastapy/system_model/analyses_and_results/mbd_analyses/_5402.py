"""AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5427,
        _5447,
        _5449,
        _5495,
        _5511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7568, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
)


class AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
    _5438.ConnectionMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5438.ConnectionMultibodyDynamicsAnalysis":
            return self._parent._cast(_5438.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_7568.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7568

            return self._parent._cast(_7568.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5427.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(_5427.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5447.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5447

            return self._parent._cast(
                _5447.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5449.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5449

            return self._parent._cast(
                _5449.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5495.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "_5511.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5511

            return self._parent._cast(
                _5511.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2283.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis(
            self
        )
