"""BoltCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7457,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BoltCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2460
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7318,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BoltCompoundAdvancedSystemDeflection")


class BoltCompoundAdvancedSystemDeflection(
    _7457.ComponentCompoundAdvancedSystemDeflection
):
    """BoltCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltCompoundAdvancedSystemDeflection")

    class _Cast_BoltCompoundAdvancedSystemDeflection:
        """Special nested class for casting BoltCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
            parent: "BoltCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_system_deflection(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolt_compound_advanced_system_deflection(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
        ) -> "BoltCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BoltCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2460.Bolt":
        """mastapy.system_model.part_model.Bolt

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7318.BoltAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BoltAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7318.BoltAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BoltAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "BoltCompoundAdvancedSystemDeflection._Cast_BoltCompoundAdvancedSystemDeflection":
        return self._Cast_BoltCompoundAdvancedSystemDeflection(self)
