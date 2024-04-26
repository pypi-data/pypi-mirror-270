"""TorqueConverterCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2911
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "TorqueConverterCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2630
    from mastapy.system_model.analyses_and_results.system_deflections import _2853
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2974,
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterCompoundSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterCompoundSystemDeflection")


class TorqueConverterCompoundSystemDeflection(_2911.CouplingCompoundSystemDeflection):
    """TorqueConverterCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterCompoundSystemDeflection"
    )

    class _Cast_TorqueConverterCompoundSystemDeflection:
        """Special nested class for casting TorqueConverterCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
            parent: "TorqueConverterCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_compound_system_deflection(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_2911.CouplingCompoundSystemDeflection":
            return self._parent._cast(_2911.CouplingCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_compound_system_deflection(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
        ) -> "TorqueConverterCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "TorqueConverterCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2630.TorqueConverter":
        """mastapy.system_model.part_model.couplings.TorqueConverter

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
    ) -> "List[_2853.TorqueConverterSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection]

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
    ) -> "List[_2853.TorqueConverterSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterSystemDeflection]

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
    ) -> "TorqueConverterCompoundSystemDeflection._Cast_TorqueConverterCompoundSystemDeflection":
        return self._Cast_TorqueConverterCompoundSystemDeflection(self)
