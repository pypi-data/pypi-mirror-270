"""MeasurementComponentCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7554,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "MeasurementComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7378,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundAdvancedSystemDeflection")


class MeasurementComponentCompoundAdvancedSystemDeflection(
    _7554.VirtualComponentCompoundAdvancedSystemDeflection
):
    """MeasurementComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_MeasurementComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting MeasurementComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
            parent: "MeasurementComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7554.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7554.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
        ) -> "MeasurementComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "MeasurementComponentCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

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
    ) -> "List[_7378.MeasurementComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.MeasurementComponentAdvancedSystemDeflection]

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
    ) -> "List[_7378.MeasurementComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.MeasurementComponentAdvancedSystemDeflection]

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
    ) -> "MeasurementComponentCompoundAdvancedSystemDeflection._Cast_MeasurementComponentCompoundAdvancedSystemDeflection":
        return self._Cast_MeasurementComponentCompoundAdvancedSystemDeflection(self)
