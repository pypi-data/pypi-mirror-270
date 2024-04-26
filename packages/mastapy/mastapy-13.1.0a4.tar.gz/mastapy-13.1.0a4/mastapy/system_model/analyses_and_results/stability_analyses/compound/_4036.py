"""SynchroniserSleeveCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4035
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SynchroniserSleeveCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2629
    from mastapy.system_model.analyses_and_results.stability_analyses import _3906
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3959,
        _3997,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveCompoundStabilityAnalysis")


class SynchroniserSleeveCompoundStabilityAnalysis(
    _4035.SynchroniserPartCompoundStabilityAnalysis
):
    """SynchroniserSleeveCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveCompoundStabilityAnalysis"
    )

    class _Cast_SynchroniserSleeveCompoundStabilityAnalysis:
        """Special nested class for casting SynchroniserSleeveCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
            parent: "SynchroniserSleeveCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_4035.SynchroniserPartCompoundStabilityAnalysis":
            return self._parent._cast(_4035.SynchroniserPartCompoundStabilityAnalysis)

        @property
        def coupling_half_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_3959.CouplingHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3959,
            )

            return self._parent._cast(_3959.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
        ) -> "SynchroniserSleeveCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2629.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3906.SynchroniserSleeveStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserSleeveStabilityAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3906.SynchroniserSleeveStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserSleeveStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveCompoundStabilityAnalysis._Cast_SynchroniserSleeveCompoundStabilityAnalysis":
        return self._Cast_SynchroniserSleeveCompoundStabilityAnalysis(self)
