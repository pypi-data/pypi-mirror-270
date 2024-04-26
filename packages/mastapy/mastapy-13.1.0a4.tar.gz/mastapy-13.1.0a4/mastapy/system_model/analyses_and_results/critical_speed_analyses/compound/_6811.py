"""StraightBevelGearSetCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6719,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2566
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6682
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6809,
        _6810,
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
__all__ = ("StraightBevelGearSetCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearSetCompoundCriticalSpeedAnalysis")


class StraightBevelGearSetCompoundCriticalSpeedAnalysis(
    _6719.BevelGearSetCompoundCriticalSpeedAnalysis
):
    """StraightBevelGearSetCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis"
    )

    class _Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis:
        """Special nested class for casting StraightBevelGearSetCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
            parent: "StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6719.BevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6719.BevelGearSetCompoundCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6707.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6707,
            )

            return self._parent._cast(
                _6707.AGMAGleasonConicalGearSetCompoundCriticalSpeedAnalysis
            )

        @property
        def conical_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6735.ConicalGearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6735,
            )

            return self._parent._cast(_6735.ConicalGearSetCompoundCriticalSpeedAnalysis)

        @property
        def gear_set_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6761.GearSetCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6761,
            )

            return self._parent._cast(_6761.GearSetCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_critical_speed_analysis(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
        ) -> "StraightBevelGearSetCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis",
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
        instance_to_wrap: "StraightBevelGearSetCompoundCriticalSpeedAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2566.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2566.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

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
    ) -> "List[_6682.StraightBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearSetCriticalSpeedAnalysis]

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
    def straight_bevel_gears_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6809.StraightBevelGearCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.StraightBevelGearCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_critical_speed_analysis(
        self: Self,
    ) -> "List[_6810.StraightBevelGearMeshCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.StraightBevelGearMeshCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundCriticalSpeedAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6682.StraightBevelGearSetCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.StraightBevelGearSetCriticalSpeedAnalysis]

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
    ) -> "StraightBevelGearSetCompoundCriticalSpeedAnalysis._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis":
        return self._Cast_StraightBevelGearSetCompoundCriticalSpeedAnalysis(self)
