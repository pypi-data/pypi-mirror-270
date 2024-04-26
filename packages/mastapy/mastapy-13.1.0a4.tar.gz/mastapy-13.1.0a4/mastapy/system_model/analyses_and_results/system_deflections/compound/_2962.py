"""PowerLoadCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2998
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "PowerLoadCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2490
    from mastapy.system_model.analyses_and_results.system_deflections import _2815
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2952,
        _2899,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundSystemDeflection",)


Self = TypeVar("Self", bound="PowerLoadCompoundSystemDeflection")


class PowerLoadCompoundSystemDeflection(_2998.VirtualComponentCompoundSystemDeflection):
    """PowerLoadCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PowerLoadCompoundSystemDeflection")

    class _Cast_PowerLoadCompoundSystemDeflection:
        """Special nested class for casting PowerLoadCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
            parent: "PowerLoadCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_system_deflection(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_2998.VirtualComponentCompoundSystemDeflection":
            return self._parent._cast(_2998.VirtualComponentCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_2952.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_2899.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def power_load_compound_system_deflection(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
        ) -> "PowerLoadCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundSystemDeflection.TYPE"
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
    ) -> "List[_2815.PowerLoadSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection]

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
    def component_analysis_cases(self: Self) -> "List[_2815.PowerLoadSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.PowerLoadSystemDeflection]

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
    ) -> "PowerLoadCompoundSystemDeflection._Cast_PowerLoadCompoundSystemDeflection":
        return self._Cast_PowerLoadCompoundSystemDeflection(self)
