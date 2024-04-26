"""StraightBevelPlanetGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7407
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "StraightBevelPlanetGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7315,
        _7303,
        _7331,
        _7359,
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearAdvancedSystemDeflection")


class StraightBevelPlanetGearAdvancedSystemDeflection(
    _7407.StraightBevelDiffGearAdvancedSystemDeflection
):
    """StraightBevelPlanetGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearAdvancedSystemDeflection"
    )

    class _Cast_StraightBevelPlanetGearAdvancedSystemDeflection:
        """Special nested class for casting StraightBevelPlanetGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
            parent: "StraightBevelPlanetGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7407.StraightBevelDiffGearAdvancedSystemDeflection":
            return self._parent._cast(
                _7407.StraightBevelDiffGearAdvancedSystemDeflection
            )

        @property
        def bevel_gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7315.BevelGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7315,
            )

            return self._parent._cast(_7315.BevelGearAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7303.AGMAGleasonConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7303,
            )

            return self._parent._cast(
                _7303.AGMAGleasonConicalGearAdvancedSystemDeflection
            )

        @property
        def conical_gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7331.ConicalGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7331,
            )

            return self._parent._cast(_7331.ConicalGearAdvancedSystemDeflection)

        @property
        def gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7359.GearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7359,
            )

            return self._parent._cast(_7359.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_advanced_system_deflection(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
        ) -> "StraightBevelPlanetGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection",
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
        instance_to_wrap: "StraightBevelPlanetGearAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2567.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearAdvancedSystemDeflection._Cast_StraightBevelPlanetGearAdvancedSystemDeflection":
        return self._Cast_StraightBevelPlanetGearAdvancedSystemDeflection(self)
