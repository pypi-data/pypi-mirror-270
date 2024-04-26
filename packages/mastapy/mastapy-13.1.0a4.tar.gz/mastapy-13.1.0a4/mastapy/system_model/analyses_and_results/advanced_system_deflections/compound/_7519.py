"""PowerLoadCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7554,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PowerLoadCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2490
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7389,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadCompoundAdvancedSystemDeflection")


class PowerLoadCompoundAdvancedSystemDeflection(
    _7554.VirtualComponentCompoundAdvancedSystemDeflection
):
    """PowerLoadCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundAdvancedSystemDeflection"
    )

    class _Cast_PowerLoadCompoundAdvancedSystemDeflection:
        """Special nested class for casting PowerLoadCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
            parent: "PowerLoadCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7554.VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7554.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
        ) -> "PowerLoadCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2490.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_7389.PowerLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PowerLoadAdvancedSystemDeflection]

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
    ) -> "List[_7389.PowerLoadAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PowerLoadAdvancedSystemDeflection]

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
    ) -> "PowerLoadCompoundAdvancedSystemDeflection._Cast_PowerLoadCompoundAdvancedSystemDeflection":
        return self._Cast_PowerLoadCompoundAdvancedSystemDeflection(self)
