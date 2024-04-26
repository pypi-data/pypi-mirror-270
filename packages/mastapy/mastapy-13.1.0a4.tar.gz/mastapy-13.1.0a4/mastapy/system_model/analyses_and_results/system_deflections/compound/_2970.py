"""ShaftCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ShaftCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2500
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2971,
        _2876,
        _2899,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2827
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ShaftCompoundSystemDeflection")


class ShaftCompoundSystemDeflection(_2875.AbstractShaftCompoundSystemDeflection):
    """ShaftCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundSystemDeflection")

    class _Cast_ShaftCompoundSystemDeflection:
        """Special nested class for casting ShaftCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
            parent: "ShaftCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_system_deflection(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_2875.AbstractShaftCompoundSystemDeflection":
            return self._parent._cast(_2875.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_2876.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(
                _2876.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def component_compound_system_deflection(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_2899.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def shaft_compound_system_deflection(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
        ) -> "ShaftCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2500.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def shaft_duty_cycle_damage_results(
        self: Self,
    ) -> "_2971.ShaftDutyCycleSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftDutyCycleSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftDutyCycleDamageResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2827.ShaftSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection]

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
    def planetaries(self: Self) -> "List[ShaftCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ShaftCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_2827.ShaftSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ShaftSystemDeflection]

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
    ) -> "ShaftCompoundSystemDeflection._Cast_ShaftCompoundSystemDeflection":
        return self._Cast_ShaftCompoundSystemDeflection(self)
