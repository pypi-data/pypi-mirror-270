"""HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
        "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7563,
        _7576,
        _7561,
    )
    from mastapy.system_model.analyses_and_results import _2673


__docformat__ = "restructuredtext en"
__all__ = ("HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation"
)


class HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
    _5787.HarmonicAnalysis
):
    """HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _HARMONIC_ANALYSIS_FOR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
            parent: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def harmonic_analysis(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_5787.HarmonicAnalysis":
            return self._parent._cast(_5787.HarmonicAnalysis)

        @property
        def compound_analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7563.CompoundAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7563

            return self._parent._cast(_7563.CompoundAnalysisCase)

        @property
        def static_load_analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7576.StaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7576

            return self._parent._cast(_7576.StaticLoadAnalysisCase)

        @property
        def analysis_case(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7561.AnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7561

            return self._parent._cast(_7561.AnalysisCase)

        @property
        def context(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2673.Context":
            from mastapy.system_model.analyses_and_results import _2673

            return self._parent._cast(_2673.Context)

        @property
        def harmonic_analysis_for_advanced_time_stepping_analysis_for_modulation(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
        ) -> "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_HarmonicAnalysisForAdvancedTimeSteppingAnalysisForModulation(
            self
        )
