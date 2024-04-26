"""ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7035,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2313
    from mastapy.system_model.analyses_and_results.system_deflections import _2828
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7061,
        _7082,
        _7121,
        _7072,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7035.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7035.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7061.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7061,
            )

            return self._parent._cast(
                _7061.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7121.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7121,
            )

            return self._parent._cast(
                _7121.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2828.ShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
