"""BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7171,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7053,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7178,
        _7181,
        _7182,
        _7266,
        _7272,
        _7275,
        _7278,
        _7279,
        _7293,
        _7199,
        _7225,
        _7244,
        _7192,
        _7246,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7171.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7171.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7171.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7199.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7199,
            )

            return self._parent._cast(
                _7199.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7225.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7244.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7244,
            )

            return self._parent._cast(
                _7244.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7192,
            )

            return self._parent._cast(
                _7192.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7246,
            )

            return self._parent._cast(
                _7246.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7178.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7181.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7181,
            )

            return self._parent._cast(
                _7181.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7266.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7272.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7272,
            )

            return self._parent._cast(
                _7272.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7275.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7275,
            )

            return self._parent._cast(
                _7275.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7278.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7278,
            )

            return self._parent._cast(
                _7278.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7279.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7279,
            )

            return self._parent._cast(
                _7279.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7293.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7293,
            )

            return self._parent._cast(
                _7293.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelGearAdvancedTimeSteppingAnalysisForModulation]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7053.BevelGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BevelGearAdvancedTimeSteppingAnalysisForModulation]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
