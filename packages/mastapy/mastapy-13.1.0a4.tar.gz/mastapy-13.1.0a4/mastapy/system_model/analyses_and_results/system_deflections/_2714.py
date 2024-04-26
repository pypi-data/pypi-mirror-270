"""AGMAGleasonConicalGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2749
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "AGMAGleasonConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.power_flows import _4060
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2726,
        _2727,
        _2728,
        _2731,
        _2788,
        _2832,
        _2838,
        _2841,
        _2842,
        _2843,
        _2864,
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
__all__ = ("AGMAGleasonConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSystemDeflection")


class AGMAGleasonConicalGearSystemDeflection(_2749.ConicalGearSystemDeflection):
    """AGMAGleasonConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
            parent: "AGMAGleasonConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2726.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2726,
            )

            return self._parent._cast(_2726.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2727.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2728.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2788.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2788,
            )

            return self._parent._cast(_2788.HypoidGearSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2832.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.SpiralBevelGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2838,
            )

            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2841.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2841,
            )

            return self._parent._cast(_2841.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "_2864.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2864,
            )

            return self._parent._cast(_2864.ZerolBevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
        ) -> "AGMAGleasonConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2531.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4060.AGMAGleasonConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.AGMAGleasonConicalGearPowerFlow

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
    ) -> "AGMAGleasonConicalGearSystemDeflection._Cast_AGMAGleasonConicalGearSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSystemDeflection(self)
