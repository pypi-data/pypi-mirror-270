"""KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7498,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2558
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7373,
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
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection(
    _7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> (
            "_7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            return self._parent._cast(
                _7498.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7490.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2558.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

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
    ) -> "List[_7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]

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
    ) -> "List[_7373.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection(
            self
        )
