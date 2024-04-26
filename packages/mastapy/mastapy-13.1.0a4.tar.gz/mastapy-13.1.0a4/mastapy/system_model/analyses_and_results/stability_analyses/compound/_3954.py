"""ConicalGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3980
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConicalGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3819
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3926,
        _3933,
        _3938,
        _3984,
        _3988,
        _3991,
        _3994,
        _4021,
        _4027,
        _4030,
        _4048,
        _4018,
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetCompoundStabilityAnalysis")


class ConicalGearSetCompoundStabilityAnalysis(_3980.GearSetCompoundStabilityAnalysis):
    """ConicalGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetCompoundStabilityAnalysis"
    )

    class _Cast_ConicalGearSetCompoundStabilityAnalysis:
        """Special nested class for casting ConicalGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
            parent: "ConicalGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3926,
            )

            return self._parent._cast(
                _3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_differential_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3933.BevelDifferentialGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3933,
            )

            return self._parent._cast(
                _3933.BevelDifferentialGearSetCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3938.BevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3938,
            )

            return self._parent._cast(_3938.BevelGearSetCompoundStabilityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3984.HypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3984,
            )

            return self._parent._cast(_3984.HypoidGearSetCompoundStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3988,
            )

            return self._parent._cast(
                _3988.KlingelnbergCycloPalloidConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3991,
            )

            return self._parent._cast(
                _3991.KlingelnbergCycloPalloidHypoidGearSetCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> (
            "_3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3994,
            )

            return self._parent._cast(
                _3994.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4021.SpiralBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4021,
            )

            return self._parent._cast(_4021.SpiralBevelGearSetCompoundStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4027.StraightBevelDiffGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4027,
            )

            return self._parent._cast(
                _4027.StraightBevelDiffGearSetCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4030.StraightBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4030,
            )

            return self._parent._cast(
                _4030.StraightBevelGearSetCompoundStabilityAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "_4048.ZerolBevelGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4048,
            )

            return self._parent._cast(_4048.ZerolBevelGearSetCompoundStabilityAnalysis)

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
        ) -> "ConicalGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3819.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    ) -> "List[_3819.ConicalGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConicalGearSetStabilityAnalysis]

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
    ) -> "ConicalGearSetCompoundStabilityAnalysis._Cast_ConicalGearSetCompoundStabilityAnalysis":
        return self._Cast_ConicalGearSetCompoundStabilityAnalysis(self)
