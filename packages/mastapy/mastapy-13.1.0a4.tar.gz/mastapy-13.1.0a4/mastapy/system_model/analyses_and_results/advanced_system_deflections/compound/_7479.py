"""CylindricalGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7490,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "CylindricalGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.gears.rating.cylindrical import _462
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7347,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7482,
        _7509,
        _7457,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearCompoundAdvancedSystemDeflection")


class CylindricalGearCompoundAdvancedSystemDeflection(
    _7490.GearCompoundAdvancedSystemDeflection
):
    """CylindricalGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
            parent: "CylindricalGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7490.GearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7490.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7509.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7457.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(_7457.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "_7482.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
        ) -> "CylindricalGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "CylindricalGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_duty_cycle_rating(self: Self) -> "_462.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_rating(self: Self) -> "_462.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7347.CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

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
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.CylindricalGearCompoundAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7347.CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

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
    ) -> "CylindricalGearCompoundAdvancedSystemDeflection._Cast_CylindricalGearCompoundAdvancedSystemDeflection":
        return self._Cast_CylindricalGearCompoundAdvancedSystemDeflection(self)
