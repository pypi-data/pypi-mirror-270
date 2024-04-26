"""ConceptCouplingConnectionCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7470,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2362
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7326,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7497,
        _7467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionCompoundAdvancedSystemDeflection"
)


class ConceptCouplingConnectionCompoundAdvancedSystemDeflection(
    _7470.CouplingConnectionCompoundAdvancedSystemDeflection
):
    """ConceptCouplingConnectionCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
    )

    class _Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingConnectionCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
            parent: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7470.CouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7470.CouplingConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(
                _7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7467.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_advanced_system_deflection(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
        ) -> "ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2362.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2362.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

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
    ) -> "List[_7326.ConceptCouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingConnectionAdvancedSystemDeflection]

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
    ) -> "List[_7326.ConceptCouplingConnectionAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingConnectionAdvancedSystemDeflection]

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
    ) -> "ConceptCouplingConnectionCompoundAdvancedSystemDeflection._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingConnectionCompoundAdvancedSystemDeflection(
            self
        )
