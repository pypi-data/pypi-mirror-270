"""AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7334
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7323,
        _7345,
        _7346,
        _7385,
        _7399,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection"
)


class AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(
    _7334.ConnectionAdvancedSystemDeflection
):
    """AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
            parent: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7334.ConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7334.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7323.CoaxialConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7323,
            )

            return self._parent._cast(_7323.CoaxialConnectionAdvancedSystemDeflection)

        @property
        def cycloidal_disc_central_bearing_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7345.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7345,
            )

            return self._parent._cast(
                _7345.CycloidalDiscCentralBearingConnectionAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7346.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7346,
            )

            return self._parent._cast(
                _7346.CycloidalDiscPlanetaryBearingConnectionAdvancedSystemDeflection
            )

        @property
        def planetary_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7385.PlanetaryConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7385,
            )

            return self._parent._cast(_7385.PlanetaryConnectionAdvancedSystemDeflection)

        @property
        def shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7399.ShaftToMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7399,
            )

            return self._parent._cast(
                _7399.ShaftToMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_system_deflection(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection.TYPE",
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
    ) -> "AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_AbstractShaftToMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
