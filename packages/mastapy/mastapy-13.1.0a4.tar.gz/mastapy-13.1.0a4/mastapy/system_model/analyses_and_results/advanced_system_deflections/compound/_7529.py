"""ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7435,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7399,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7456,
        _7476,
        _7515,
        _7467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection"
)


class ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(
    _7435.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
):
    """ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
            parent: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7435.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7435.AbstractShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7467.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7456.CoaxialConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7456,
            )

            return self._parent._cast(
                _7456.CoaxialConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7476.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.CycloidalDiscCentralBearingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7515.PlanetaryConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.PlanetaryConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_to_mountable_component_connection_compound_advanced_system_deflection(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
        ) -> "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7399.ShaftToMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ShaftToMountableComponentConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7399.ShaftToMountableComponentConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ShaftToMountableComponentConnectionAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_ShaftToMountableComponentConnectionCompoundAdvancedSystemDeflection(
            self
        )
