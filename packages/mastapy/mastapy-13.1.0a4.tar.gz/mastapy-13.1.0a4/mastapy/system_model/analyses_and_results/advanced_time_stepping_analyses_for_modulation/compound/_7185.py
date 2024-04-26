"""BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7173,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7055,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7180,
        _7268,
        _7274,
        _7277,
        _7295,
        _7201,
        _7227,
        _7265,
        _7167,
        _7246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7173.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7173.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7173.AGMAGleasonConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.ConicalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7227.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7227,
            )

            return self._parent._cast(
                _7227.GearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def specialised_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7265.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.SpecialisedAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7167.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7167,
            )

            return self._parent._cast(
                _7167.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7180.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7180,
            )

            return self._parent._cast(
                _7180.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7268.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7268,
            )

            return self._parent._cast(
                _7268.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7274.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7274,
            )

            return self._parent._cast(
                _7274.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7277.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7277,
            )

            return self._parent._cast(
                _7277.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7295.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7295,
            )

            return self._parent._cast(
                _7295.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_set_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7055.BevelGearSetAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelGearSetAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
