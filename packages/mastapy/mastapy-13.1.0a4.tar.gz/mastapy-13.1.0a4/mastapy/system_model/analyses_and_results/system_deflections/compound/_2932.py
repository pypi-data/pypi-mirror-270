"""FlexiblePinAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "FlexiblePinAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.system_deflections import _2781
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundSystemDeflection")


class FlexiblePinAssemblyCompoundSystemDeflection(
    _2974.SpecialisedAssemblyCompoundSystemDeflection
):
    """FlexiblePinAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundSystemDeflection"
    )

    class _Cast_FlexiblePinAssemblyCompoundSystemDeflection:
        """Special nested class for casting FlexiblePinAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
            parent: "FlexiblePinAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_system_deflection(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
        ) -> "FlexiblePinAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "FlexiblePinAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2781.FlexiblePinAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2781.FlexiblePinAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.FlexiblePinAssemblySystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyCompoundSystemDeflection._Cast_FlexiblePinAssemblyCompoundSystemDeflection":
        return self._Cast_FlexiblePinAssemblyCompoundSystemDeflection(self)
