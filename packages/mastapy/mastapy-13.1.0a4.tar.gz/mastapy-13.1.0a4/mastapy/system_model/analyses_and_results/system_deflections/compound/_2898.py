"""CoaxialConnectionCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2973
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CoaxialConnectionCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2287
    from mastapy.system_model.analyses_and_results.system_deflections import _2737
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2918,
        _2877,
        _2909,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundSystemDeflection")


class CoaxialConnectionCompoundSystemDeflection(
    _2973.ShaftToMountableComponentConnectionCompoundSystemDeflection
):
    """CoaxialConnectionCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundSystemDeflection"
    )

    class _Cast_CoaxialConnectionCompoundSystemDeflection:
        """Special nested class for casting CoaxialConnectionCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
            parent: "CoaxialConnectionCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_2973.ShaftToMountableComponentConnectionCompoundSystemDeflection":
            return self._parent._cast(
                _2973.ShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> (
            "_2877.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2877,
            )

            return self._parent._cast(
                _2877.AbstractShaftToMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_2909.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "_2918.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2918,
            )

            return self._parent._cast(
                _2918.CycloidalDiscCentralBearingConnectionCompoundSystemDeflection
            )

        @property
        def coaxial_connection_compound_system_deflection(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
        ) -> "CoaxialConnectionCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2287.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2737.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2737.CoaxialConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CoaxialConnectionSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CoaxialConnectionCompoundSystemDeflection._Cast_CoaxialConnectionCompoundSystemDeflection":
        return self._Cast_CoaxialConnectionCompoundSystemDeflection(self)
