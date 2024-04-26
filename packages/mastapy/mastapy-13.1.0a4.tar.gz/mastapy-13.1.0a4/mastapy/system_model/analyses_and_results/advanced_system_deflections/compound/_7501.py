"""KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7498,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7370,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7464,
        _7490,
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection(
    _7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> (
            "_7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            return self._parent._cast(
                _7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7490.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2556.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

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
    ) -> "List[_7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]

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
    ) -> "List[_7370.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidHypoidGearAdvancedSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection(
            self
        )
