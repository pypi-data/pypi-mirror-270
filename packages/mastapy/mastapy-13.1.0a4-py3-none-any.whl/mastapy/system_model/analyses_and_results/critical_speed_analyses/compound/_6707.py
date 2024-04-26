"""AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6735,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6575
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6714,
        _6719,
        _6765,
        _6802,
        _6808,
        _6811,
        _6829,
        _6761,
        _6799,
        _6701,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis")


class AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis(
    _6735.ConicalGearSetCompoundCriticalSpeedAnalysis
):
    """AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6735.ConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6735.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6761.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6714.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6714,
            )

            return self._parent._cast(
                _6714.BevelDifferentialGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6719.BevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6719,
            )

            return self._parent._cast(_6719.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6765.HypoidGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6765,
            )

            return self._parent._cast(_6765.HypoidGearSetCompoundCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6802.SpiralBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6802,
            )

            return self._parent._cast(
                _6802.SpiralBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6808.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6808,
            )

            return self._parent._cast(
                _6808.StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6811.StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6811,
            )

            return self._parent._cast(
                _6811.StraightBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6829.ZerolBevelGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6829,
            )

            return self._parent._cast(
                _6829.ZerolBevelGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]

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
    ) -> "List[_6575.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AGMAGleasonConicalGearSetCriticalSpeedAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis(self)
