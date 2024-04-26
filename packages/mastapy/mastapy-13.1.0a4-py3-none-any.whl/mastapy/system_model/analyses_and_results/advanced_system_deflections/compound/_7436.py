"""AGMAGleasonConicalGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7464,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7303,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7443,
        _7446,
        _7447,
        _7448,
        _7494,
        _7531,
        _7537,
        _7540,
        _7543,
        _7544,
        _7558,
        _7490,
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearCompoundAdvancedSystemDeflection")


class AGMAGleasonConicalGearCompoundAdvancedSystemDeflection(
    _7464.ConicalGearCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7464.ConicalGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7464.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7490.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(_7490.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7443.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7443,
            )

            return self._parent._cast(
                _7443.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7446.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7446,
            )

            return self._parent._cast(
                _7446.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7447.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7448.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7448,
            )

            return self._parent._cast(_7448.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7494.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7531.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(
                _7531.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7537.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7537,
            )

            return self._parent._cast(
                _7537.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7540.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7540,
            )

            return self._parent._cast(
                _7540.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7543.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7543,
            )

            return self._parent._cast(
                _7543.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7544.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7544,
            )

            return self._parent._cast(
                _7544.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "_7558.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7558,
            )

            return self._parent._cast(
                _7558.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7303.AGMAGleasonConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearAdvancedSystemDeflection]

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
    ) -> "List[_7303.AGMAGleasonConicalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearAdvancedSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearCompoundAdvancedSystemDeflection(self)
