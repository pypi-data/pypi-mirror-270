"""RootAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "RootAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2492
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6609,
        _6569,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCriticalSpeedAnalysis")


class RootAssemblyCriticalSpeedAnalysis(_6576.AssemblyCriticalSpeedAnalysis):
    """RootAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyCriticalSpeedAnalysis")

    class _Cast_RootAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting RootAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
            parent: "RootAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_critical_speed_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_6576.AssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6576.AssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_6569.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_critical_speed_analysis(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
        ) -> "RootAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RootAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2492.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def critical_speed_analysis_inputs(self: Self) -> "_6609.CriticalSpeedAnalysis":
        """mastapy.system_model.analyses_and_results.critical_speed_analyses.CriticalSpeedAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CriticalSpeedAnalysisInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCriticalSpeedAnalysis._Cast_RootAssemblyCriticalSpeedAnalysis":
        return self._Cast_RootAssemblyCriticalSpeedAnalysis(self)
