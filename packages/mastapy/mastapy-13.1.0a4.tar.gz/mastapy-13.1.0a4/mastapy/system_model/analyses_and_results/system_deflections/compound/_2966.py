"""RollingRingAssemblyCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2974
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "RollingRingAssemblyCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2617
    from mastapy.system_model.analyses_and_results.system_deflections import _2820
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyCompoundSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingAssemblyCompoundSystemDeflection")


class RollingRingAssemblyCompoundSystemDeflection(
    _2974.SpecialisedAssemblyCompoundSystemDeflection
):
    """RollingRingAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyCompoundSystemDeflection"
    )

    class _Cast_RollingRingAssemblyCompoundSystemDeflection:
        """Special nested class for casting RollingRingAssemblyCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
            parent: "RollingRingAssemblyCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_system_deflection(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_compound_system_deflection(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
        ) -> "RollingRingAssemblyCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2617.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

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
    ) -> "List[_2820.RollingRingAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection]

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
    ) -> "List[_2820.RollingRingAssemblySystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingAssemblySystemDeflection]

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
    ) -> "RollingRingAssemblyCompoundSystemDeflection._Cast_RollingRingAssemblyCompoundSystemDeflection":
        return self._Cast_RollingRingAssemblyCompoundSystemDeflection(self)
