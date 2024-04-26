"""SynchroniserHalfCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7547,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SynchroniserHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7416,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7471,
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundAdvancedSystemDeflection")


class SynchroniserHalfCompoundAdvancedSystemDeflection(
    _7547.SynchroniserPartCompoundAdvancedSystemDeflection
):
    """SynchroniserHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_SynchroniserHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting SynchroniserHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
            parent: "SynchroniserHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7547.SynchroniserPartCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7547.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7471.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7471,
            )

            return self._parent._cast(
                _7471.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
        ) -> "SynchroniserHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SynchroniserHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_7416.SynchroniserHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserHalfAdvancedSystemDeflection]

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
    ) -> "List[_7416.SynchroniserHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SynchroniserHalfAdvancedSystemDeflection]

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
    ) -> "SynchroniserHalfCompoundAdvancedSystemDeflection._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection":
        return self._Cast_SynchroniserHalfCompoundAdvancedSystemDeflection(self)
