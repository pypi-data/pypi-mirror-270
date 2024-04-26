"""CylindricalPlanetGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CylindricalPlanetGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2773
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2933,
        _2952,
        _2899,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundSystemDeflection")


class CylindricalPlanetGearCompoundSystemDeflection(
    _2921.CylindricalGearCompoundSystemDeflection
):
    """CylindricalPlanetGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundSystemDeflection"
    )

    class _Cast_CylindricalPlanetGearCompoundSystemDeflection:
        """Special nested class for casting CylindricalPlanetGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
            parent: "CylindricalPlanetGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2921.CylindricalGearCompoundSystemDeflection":
            return self._parent._cast(_2921.CylindricalGearCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2933.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2952.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2899.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
        ) -> "CylindricalPlanetGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2773.CylindricalPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection]

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
    ) -> "List[_2773.CylindricalPlanetGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalPlanetGearSystemDeflection]

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
    ) -> "CylindricalPlanetGearCompoundSystemDeflection._Cast_CylindricalPlanetGearCompoundSystemDeflection":
        return self._Cast_CylindricalPlanetGearCompoundSystemDeflection(self)
