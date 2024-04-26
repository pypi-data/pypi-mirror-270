"""AbstractShaftToMountableComponentConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3821
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
        "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3810,
        _3831,
        _3832,
        _3871,
        _3885,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionStabilityAnalysis",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionStabilityAnalysis"
)


class AbstractShaftToMountableComponentConnectionStabilityAnalysis(
    _3821.ConnectionStabilityAnalysis
):
    """AbstractShaftToMountableComponentConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3821.ConnectionStabilityAnalysis":
            return self._parent._cast(_3821.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3810.CoaxialConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CoaxialConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3831.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(
                _3831.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3832.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3871.PlanetaryConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.PlanetaryConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "_3885.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(
                _3885.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionStabilityAnalysis.TYPE",
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
    ) -> "AbstractShaftToMountableComponentConnectionStabilityAnalysis._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionStabilityAnalysis(
            self
        )
