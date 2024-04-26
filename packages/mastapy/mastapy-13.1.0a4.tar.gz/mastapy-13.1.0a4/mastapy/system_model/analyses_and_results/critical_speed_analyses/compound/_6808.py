"""StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6719,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2564
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6679
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6806,
        _6807,
        _6707,
        _6735,
        _6761,
        _6799,
        _6701,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis")


class StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis(
    _6719.BevelGearSetCompoundCriticalSpeedAnalysis
):
    """StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6719.BevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6719.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6707.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6735.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6761.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6679.StraightBevelDiffGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearSetCriticalSpeedAnalysis]

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
    def straight_bevel_diff_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6806.StraightBevelDiffGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.StraightBevelDiffGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6807.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.StraightBevelDiffGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6679.StraightBevelDiffGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelDiffGearSetCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundCriticalSpeedAnalysis(self)
