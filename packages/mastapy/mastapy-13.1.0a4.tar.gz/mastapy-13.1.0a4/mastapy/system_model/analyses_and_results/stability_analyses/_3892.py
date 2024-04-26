"""SpringDamperStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3825
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SpringDamperStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2623
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3886,
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperStabilityAnalysis",)


Self = TypeVar("Self", bound="SpringDamperStabilityAnalysis")


class SpringDamperStabilityAnalysis(_3825.CouplingStabilityAnalysis):
    """SpringDamperStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperStabilityAnalysis")

    class _Cast_SpringDamperStabilityAnalysis:
        """Special nested class for casting SpringDamperStabilityAnalysis to subclasses."""

        def __init__(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
            parent: "SpringDamperStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3825.CouplingStabilityAnalysis":
            return self._parent._cast(_3825.CouplingStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_stability_analysis(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
        ) -> "SpringDamperStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2623.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6985.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

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
    ) -> "SpringDamperStabilityAnalysis._Cast_SpringDamperStabilityAnalysis":
        return self._Cast_SpringDamperStabilityAnalysis(self)
