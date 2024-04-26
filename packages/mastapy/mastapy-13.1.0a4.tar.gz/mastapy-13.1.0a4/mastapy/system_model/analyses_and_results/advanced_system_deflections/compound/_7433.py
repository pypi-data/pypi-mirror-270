"""AbstractShaftCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7434,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AbstractShaftCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7297,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7477,
        _7527,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftCompoundAdvancedSystemDeflection")


class AbstractShaftCompoundAdvancedSystemDeflection(
    _7434.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
):
    """AbstractShaftCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundAdvancedSystemDeflection"
    )

    class _Cast_AbstractShaftCompoundAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
            parent: "AbstractShaftCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7434.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7434.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7477.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "_7527.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(_7527.ShaftCompoundAdvancedSystemDeflection)

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
        ) -> "AbstractShaftCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AbstractShaftCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7297.AbstractShaftAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7297.AbstractShaftAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AbstractShaftAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundAdvancedSystemDeflection._Cast_AbstractShaftCompoundAdvancedSystemDeflection":
        return self._Cast_AbstractShaftCompoundAdvancedSystemDeflection(self)
