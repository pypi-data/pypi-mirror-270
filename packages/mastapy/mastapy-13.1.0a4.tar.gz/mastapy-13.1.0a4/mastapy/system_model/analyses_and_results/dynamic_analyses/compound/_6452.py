"""BevelGearSetCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6440
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelGearSetCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6447,
        _6535,
        _6541,
        _6544,
        _6562,
        _6468,
        _6494,
        _6532,
        _6434,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundDynamicAnalysis")


class BevelGearSetCompoundDynamicAnalysis(
    _6440.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
):
    """BevelGearSetCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundDynamicAnalysis")

    class _Cast_BevelGearSetCompoundDynamicAnalysis:
        """Special nested class for casting BevelGearSetCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
            parent: "BevelGearSetCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6440.AGMAGleasonConicalGearSetCompoundDynamicAnalysis":
            return self._parent._cast(
                _6440.AGMAGleasonConicalGearSetCompoundDynamicAnalysis
            )

        @property
        def conical_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6468.ConicalGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6468,
            )

            return self._parent._cast(_6468.ConicalGearSetCompoundDynamicAnalysis)

        @property
        def gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6494.GearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6494,
            )

            return self._parent._cast(_6494.GearSetCompoundDynamicAnalysis)

        @property
        def specialised_assembly_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6532.SpecialisedAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6532,
            )

            return self._parent._cast(_6532.SpecialisedAssemblyCompoundDynamicAnalysis)

        @property
        def abstract_assembly_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6434.AbstractAssemblyCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6434,
            )

            return self._parent._cast(_6434.AbstractAssemblyCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6447.BevelDifferentialGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6447,
            )

            return self._parent._cast(
                _6447.BevelDifferentialGearSetCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6535.SpiralBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6535,
            )

            return self._parent._cast(_6535.SpiralBevelGearSetCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6541.StraightBevelDiffGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6541,
            )

            return self._parent._cast(
                _6541.StraightBevelDiffGearSetCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6544.StraightBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6544,
            )

            return self._parent._cast(_6544.StraightBevelGearSetCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "_6562.ZerolBevelGearSetCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6562,
            )

            return self._parent._cast(_6562.ZerolBevelGearSetCompoundDynamicAnalysis)

        @property
        def bevel_gear_set_compound_dynamic_analysis(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
        ) -> "BevelGearSetCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6321.BevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis]

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
    ) -> "List[_6321.BevelGearSetDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearSetDynamicAnalysis]

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
    ) -> (
        "BevelGearSetCompoundDynamicAnalysis._Cast_BevelGearSetCompoundDynamicAnalysis"
    ):
        return self._Cast_BevelGearSetCompoundDynamicAnalysis(self)
