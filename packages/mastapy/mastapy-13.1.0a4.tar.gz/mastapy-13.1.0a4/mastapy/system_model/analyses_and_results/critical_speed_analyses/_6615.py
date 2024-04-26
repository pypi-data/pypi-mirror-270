"""CycloidalAssemblyCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "CycloidalAssemblyCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6569,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CycloidalAssemblyCriticalSpeedAnalysis")


class CycloidalAssemblyCriticalSpeedAnalysis(
    _6670.SpecialisedAssemblyCriticalSpeedAnalysis
):
    """CycloidalAssemblyCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalAssemblyCriticalSpeedAnalysis"
    )

    class _Cast_CycloidalAssemblyCriticalSpeedAnalysis:
        """Special nested class for casting CycloidalAssemblyCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
            parent: "CycloidalAssemblyCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_critical_speed_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_6670.SpecialisedAssemblyCriticalSpeedAnalysis":
            return self._parent._cast(_6670.SpecialisedAssemblyCriticalSpeedAnalysis)

        @property
        def abstract_assembly_critical_speed_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_6569.AbstractAssemblyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6569,
            )

            return self._parent._cast(_6569.AbstractAssemblyCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_critical_speed_analysis(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
        ) -> "CycloidalAssemblyCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalAssemblyCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalAssemblyCriticalSpeedAnalysis._Cast_CycloidalAssemblyCriticalSpeedAnalysis":
        return self._Cast_CycloidalAssemblyCriticalSpeedAnalysis(self)
