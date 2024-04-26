"""VirtualComponentCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7509,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "VirtualComponentCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7425,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7507,
        _7508,
        _7518,
        _7519,
        _7553,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundAdvancedSystemDeflection")


class VirtualComponentCompoundAdvancedSystemDeflection(
    _7509.MountableComponentCompoundAdvancedSystemDeflection
):
    """VirtualComponentCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundAdvancedSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundAdvancedSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
            parent: "VirtualComponentCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7507.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(_7507.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7508.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7508,
            )

            return self._parent._cast(
                _7508.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7518.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(_7518.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7519.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(_7519.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "_7553.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7553,
            )

            return self._parent._cast(
                _7553.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
        ) -> "VirtualComponentCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "VirtualComponentCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7425.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7425.VirtualComponentAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.VirtualComponentAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundAdvancedSystemDeflection._Cast_VirtualComponentCompoundAdvancedSystemDeflection":
        return self._Cast_VirtualComponentCompoundAdvancedSystemDeflection(self)
