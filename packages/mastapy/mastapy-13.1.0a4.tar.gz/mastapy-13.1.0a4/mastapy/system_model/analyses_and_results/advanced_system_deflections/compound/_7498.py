"""KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7464,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7367,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7501,
        _7504,
        _7490,
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection(
    _7464.ConicalGearCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.ConicalGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7464.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7490.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7501.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7501,
            )

            return self._parent._cast(
                _7501.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7504.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]

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
    ) -> "List[_7367.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidConicalGearAdvancedSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection(
            self
        )
