"""FlexiblePinAssemblyCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4018
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "FlexiblePinAssemblyCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2472
    from mastapy.system_model.analyses_and_results.stability_analyses import _3845
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="FlexiblePinAssemblyCompoundStabilityAnalysis")


class FlexiblePinAssemblyCompoundStabilityAnalysis(
    _4018.SpecialisedAssemblyCompoundStabilityAnalysis
):
    """FlexiblePinAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FlexiblePinAssemblyCompoundStabilityAnalysis"
    )

    class _Cast_FlexiblePinAssemblyCompoundStabilityAnalysis:
        """Special nested class for casting FlexiblePinAssemblyCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
            parent: "FlexiblePinAssemblyCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_stability_analysis(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
        ) -> "FlexiblePinAssemblyCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis",
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
        instance_to_wrap: "FlexiblePinAssemblyCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2472.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

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
    ) -> "List[_3845.FlexiblePinAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FlexiblePinAssemblyStabilityAnalysis]

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
    ) -> "List[_3845.FlexiblePinAssemblyStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FlexiblePinAssemblyStabilityAnalysis]

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
    ) -> "FlexiblePinAssemblyCompoundStabilityAnalysis._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis":
        return self._Cast_FlexiblePinAssemblyCompoundStabilityAnalysis(self)
