"""PartToPartShearCouplingCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PartToPartShearCouplingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2607
    from mastapy.system_model.analyses_and_results.system_deflections import _2811
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2974,
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundSystemDeflection")


class PartToPartShearCouplingCompoundSystemDeflection(
    _2911.CouplingCompoundSystemDeflection
):
    """PartToPartShearCouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingCompoundSystemDeflection"
    )

    class _Cast_PartToPartShearCouplingCompoundSystemDeflection:
        """Special nested class for casting PartToPartShearCouplingCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
            parent: "PartToPartShearCouplingCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_system_deflection(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_2911.CouplingCompoundSystemDeflection":
            return self._parent._cast(_2911.CouplingCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_system_deflection(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
        ) -> "PartToPartShearCouplingCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2607.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2607.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

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
    ) -> "List[_2811.PartToPartShearCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection]

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
    ) -> "List[_2811.PartToPartShearCouplingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingSystemDeflection]

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
    ) -> "PartToPartShearCouplingCompoundSystemDeflection._Cast_PartToPartShearCouplingCompoundSystemDeflection":
        return self._Cast_PartToPartShearCouplingCompoundSystemDeflection(self)
