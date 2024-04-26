"""SpiralBevelGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3936
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SpiralBevelGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2561
    from mastapy.system_model.analyses_and_results.stability_analyses import _3889
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3924,
        _3952,
        _3978,
        _3997,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundStabilityAnalysis")


class SpiralBevelGearCompoundStabilityAnalysis(
    _3936.BevelGearCompoundStabilityAnalysis
):
    """SpiralBevelGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearCompoundStabilityAnalysis"
    )

    class _Cast_SpiralBevelGearCompoundStabilityAnalysis:
        """Special nested class for casting SpiralBevelGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
            parent: "SpiralBevelGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3936.BevelGearCompoundStabilityAnalysis":
            return self._parent._cast(_3936.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3924.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(
                _3924.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3952.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3952,
            )

            return self._parent._cast(_3952.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3978.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_stability_analysis(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
        ) -> "SpiralBevelGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2561.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_3889.SpiralBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearStabilityAnalysis]

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
    ) -> "List[_3889.SpiralBevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SpiralBevelGearStabilityAnalysis]

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
    ) -> "SpiralBevelGearCompoundStabilityAnalysis._Cast_SpiralBevelGearCompoundStabilityAnalysis":
        return self._Cast_SpiralBevelGearCompoundStabilityAnalysis(self)
