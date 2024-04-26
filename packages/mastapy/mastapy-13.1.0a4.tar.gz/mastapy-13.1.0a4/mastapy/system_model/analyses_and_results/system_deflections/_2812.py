"""PlanetaryConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PlanetaryConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2305
    from mastapy.system_model.analyses_and_results.static_loads import _6959
    from mastapy.system_model.analyses_and_results.power_flows import _4141
    from mastapy.system_model.analyses_and_results.system_deflections import (
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
__all__ = ("PlanetaryConnectionSystemDeflection",)


Self = TypeVar("Self", bound="PlanetaryConnectionSystemDeflection")


class PlanetaryConnectionSystemDeflection(
    _2828.ShaftToMountableComponentConnectionSystemDeflection
):
    """PlanetaryConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryConnectionSystemDeflection")

    class _Cast_PlanetaryConnectionSystemDeflection:
        """Special nested class for casting PlanetaryConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
            parent: "PlanetaryConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2828.ShaftToMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2828.ShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2711.AbstractShaftToMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(
                _2711.AbstractShaftToMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_connection_system_deflection(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
        ) -> "PlanetaryConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6959.PlanetaryConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetaryConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4141.PlanetaryConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PlanetaryConnectionPowerFlow

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
    ) -> (
        "PlanetaryConnectionSystemDeflection._Cast_PlanetaryConnectionSystemDeflection"
    ):
        return self._Cast_PlanetaryConnectionSystemDeflection(self)
