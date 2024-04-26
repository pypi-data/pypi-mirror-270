"""AGMAGleasonConicalGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3954
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3791
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3933,
        _3938,
        _3984,
        _4021,
        _4027,
        _4030,
        _4048,
        _3980,
        _4018,
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundStabilityAnalysis")


class AGMAGleasonConicalGearSetCompoundStabilityAnalysis(
    _3954.ConicalGearSetCompoundStabilityAnalysis
):
    """AGMAGleasonConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3954.ConicalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3954.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3938.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3984.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4021.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4048.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4048,
            )

            return self._parent._cast(_4048.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3791.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3791.AGMAGleasonConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.AGMAGleasonConicalGearSetStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundStabilityAnalysis._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundStabilityAnalysis(self)
