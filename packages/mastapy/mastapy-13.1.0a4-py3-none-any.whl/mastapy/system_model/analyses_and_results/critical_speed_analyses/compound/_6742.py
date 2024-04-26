"""CVTCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6711,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CVTCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6613
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6799,
        _6701,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundCriticalSpeedAnalysis")


class CVTCompoundCriticalSpeedAnalysis(_6711.BeltDriveCompoundCriticalSpeedAnalysis):
    """CVTCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundCriticalSpeedAnalysis")

    class _Cast_CVTCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CVTCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
            parent: "CVTCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_6711.BeltDriveCompoundCriticalSpeedAnalysis":
            return self._parent._cast(_6711.BeltDriveCompoundCriticalSpeedAnalysis)

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6799,
            )

            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
        ) -> "CVTCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTCompoundCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6613.CVTCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTCriticalSpeedAnalysis]

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
    def assembly_analysis_cases(self: Self) -> "List[_6613.CVTCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CVTCriticalSpeedAnalysis]

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
    ) -> "CVTCompoundCriticalSpeedAnalysis._Cast_CVTCompoundCriticalSpeedAnalysis":
        return self._Cast_CVTCompoundCriticalSpeedAnalysis(self)
