"""StraightBevelPlanetGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2838
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "StraightBevelPlanetGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2567
    from mastapy.system_model.analyses_and_results.power_flows import _4171
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2731,
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
__all__ = ("StraightBevelPlanetGearSystemDeflection",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearSystemDeflection")


class StraightBevelPlanetGearSystemDeflection(
    _2838.StraightBevelDiffGearSystemDeflection
):
    """StraightBevelPlanetGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearSystemDeflection"
    )

    class _Cast_StraightBevelPlanetGearSystemDeflection:
        """Special nested class for casting StraightBevelPlanetGearSystemDeflection to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
            parent: "StraightBevelPlanetGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2838.StraightBevelDiffGearSystemDeflection":
            return self._parent._cast(_2838.StraightBevelDiffGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2731.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2731,
            )

            return self._parent._cast(_2731.BevelGearSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2714.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.AGMAGleasonConicalGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2749.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(_2749.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2784.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2805.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2805,
            )

            return self._parent._cast(_2805.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2738.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2738,
            )

            return self._parent._cast(_2738.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
        ) -> "StraightBevelPlanetGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearSystemDeflection.TYPE"
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
    def power_flow_results(self: Self) -> "_4171.StraightBevelPlanetGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.StraightBevelPlanetGearPowerFlow

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
    ) -> "StraightBevelPlanetGearSystemDeflection._Cast_StraightBevelPlanetGearSystemDeflection":
        return self._Cast_StraightBevelPlanetGearSystemDeflection(self)
