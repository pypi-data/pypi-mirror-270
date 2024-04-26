"""BeltDriveCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6799,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "BeltDriveCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6579
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6742,
        _6701,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BeltDriveCompoundCriticalSpeedAnalysis")


class BeltDriveCompoundCriticalSpeedAnalysis(
    _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
):
    """BeltDriveCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveCompoundCriticalSpeedAnalysis"
    )

    class _Cast_BeltDriveCompoundCriticalSpeedAnalysis:
        """Special nested class for casting BeltDriveCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
            parent: "BeltDriveCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_critical_speed_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "_6742.CVTCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6742,
            )

            return self._parent._cast(_6742.CVTCompoundCriticalSpeedAnalysis)

        @property
        def belt_drive_compound_critical_speed_analysis(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
        ) -> "BeltDriveCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

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
    ) -> "List[_6579.BeltDriveCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BeltDriveCriticalSpeedAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6579.BeltDriveCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.BeltDriveCriticalSpeedAnalysis]

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
    ) -> "BeltDriveCompoundCriticalSpeedAnalysis._Cast_BeltDriveCompoundCriticalSpeedAnalysis":
        return self._Cast_BeltDriveCompoundCriticalSpeedAnalysis(self)
