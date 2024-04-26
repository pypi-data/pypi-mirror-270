"""CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7135,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.system_deflections import _2737
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7082,
        _7035,
        _7072,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7135.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7135.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7035.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7035,
            )

            return self._parent._cast(
                _7035.AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7082.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7082,
            )

            return self._parent._cast(
                _7082.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6863.CoaxialConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CoaxialConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2737.CoaxialConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection

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
    ) -> "CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
