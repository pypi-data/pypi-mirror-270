"""StraightBevelDiffGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2731
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "StraightBevelDiffGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2563
    from mastapy.gears.rating.straight_bevel_diff import _406
    from mastapy.system_model.analyses_and_results.static_loads import _6986
    from mastapy.system_model.analyses_and_results.power_flows import _4166
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2842,
        _2843,
        _2714,
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
__all__ = ("StraightBevelDiffGearSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSystemDeflection")


class StraightBevelDiffGearSystemDeflection(_2731.BevelGearSystemDeflection):
    """StraightBevelDiffGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSystemDeflection"
    )

    class _Cast_StraightBevelDiffGearSystemDeflection:
        """Special nested class for casting StraightBevelDiffGearSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
            parent: "StraightBevelDiffGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2731.BevelGearSystemDeflection":
            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2842.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "_2843.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.StraightBevelSunGearSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
        ) -> "StraightBevelDiffGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2563.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_406.StraightBevelDiffGearRating":
        """mastapy.gears.rating.straight_bevel_diff.StraightBevelDiffGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6986.StraightBevelDiffGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4166.StraightBevelDiffGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow

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
    ) -> "StraightBevelDiffGearSystemDeflection._Cast_StraightBevelDiffGearSystemDeflection":
        return self._Cast_StraightBevelDiffGearSystemDeflection(self)
