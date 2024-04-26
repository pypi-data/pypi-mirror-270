"""CycloidalDiscCentralBearingConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2737
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CycloidalDiscCentralBearingConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2353
    from mastapy.system_model.analyses_and_results.power_flows import _4099
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2828,
        _2711,
        _2750,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CycloidalDiscCentralBearingConnectionSystemDeflection")


class CycloidalDiscCentralBearingConnectionSystemDeflection(
    _2737.CoaxialConnectionSystemDeflection
):
    """CycloidalDiscCentralBearingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscCentralBearingConnectionSystemDeflection"
    )

    class _Cast_CycloidalDiscCentralBearingConnectionSystemDeflection:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
            parent: "CycloidalDiscCentralBearingConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def coaxial_connection_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2737.CoaxialConnectionSystemDeflection":
            return self._parent._cast(_2737.CoaxialConnectionSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2828.ShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2828,
            )

            return self._parent._cast(
                _2828.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2711.AbstractShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(
                _2711.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_system_deflection(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
        ) -> "CycloidalDiscCentralBearingConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2353.CycloidalDiscCentralBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscCentralBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4099.CycloidalDiscCentralBearingConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CycloidalDiscCentralBearingConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscCentralBearingConnectionSystemDeflection._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection":
        return self._Cast_CycloidalDiscCentralBearingConnectionSystemDeflection(self)
