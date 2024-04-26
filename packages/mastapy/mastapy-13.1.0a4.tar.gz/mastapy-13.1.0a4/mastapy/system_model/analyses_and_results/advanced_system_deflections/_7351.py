"""CylindricalPlanetGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7347
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalPlanetGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7359,
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalPlanetGearAdvancedSystemDeflection")


class CylindricalPlanetGearAdvancedSystemDeflection(
    _7347.CylindricalGearAdvancedSystemDeflection
):
    """CylindricalPlanetGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearAdvancedSystemDeflection"
    )

    class _Cast_CylindricalPlanetGearAdvancedSystemDeflection:
        """Special nested class for casting CylindricalPlanetGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
            parent: "CylindricalPlanetGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7347.CylindricalGearAdvancedSystemDeflection":
            return self._parent._cast(_7347.CylindricalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7359.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
        ) -> "CylindricalPlanetGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection",
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
        instance_to_wrap: "CylindricalPlanetGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.CylindricalPlanetGear":
        """mastapy.system_model.part_model.gears.CylindricalPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearAdvancedSystemDeflection._Cast_CylindricalPlanetGearAdvancedSystemDeflection":
        return self._Cast_CylindricalPlanetGearAdvancedSystemDeflection(self)
