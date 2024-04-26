"""ConceptCouplingHalfCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7471,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7327,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingHalfCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConceptCouplingHalfCompoundAdvancedSystemDeflection")


class ConceptCouplingHalfCompoundAdvancedSystemDeflection(
    _7471.CouplingHalfCompoundAdvancedSystemDeflection
):
    """ConceptCouplingHalfCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConceptCouplingHalfCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
            parent: "ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7471.CouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7471.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
        ) -> "ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConceptCouplingHalfCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.ConceptCouplingHalf":
        """mastapy.system_model.part_model.couplings.ConceptCouplingHalf

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
    ) -> "List[_7327.ConceptCouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingHalfAdvancedSystemDeflection]

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
    ) -> "List[_7327.ConceptCouplingHalfAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConceptCouplingHalfAdvancedSystemDeflection]

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
    ) -> "ConceptCouplingHalfCompoundAdvancedSystemDeflection._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection":
        return self._Cast_ConceptCouplingHalfCompoundAdvancedSystemDeflection(self)
