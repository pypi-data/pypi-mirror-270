"""BevelGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2537
    from mastapy.system_model.analyses_and_results.power_flows import _4072
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2726,
        _2727,
        _2728,
        _2832,
        _2838,
        _2841,
        _2842,
        _2843,
        _2864,
        _2749,
        _2784,
        _2805,
        _2738,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearSystemDeflection")


class BevelGearSystemDeflection(_2714.AGMAGleasonConicalGearSystemDeflection):
    """BevelGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSystemDeflection")

    class _Cast_BevelGearSystemDeflection:
        """Special nested class for casting BevelGearSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
            parent: "BevelGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection",
        ) -> "BevelGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2537.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4072.BevelGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelGearPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSystemDeflection._Cast_BevelGearSystemDeflection":
        return self._Cast_BevelGearSystemDeflection(self)
