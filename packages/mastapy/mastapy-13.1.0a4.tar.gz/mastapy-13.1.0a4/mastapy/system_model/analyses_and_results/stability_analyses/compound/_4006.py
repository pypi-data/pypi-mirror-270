"""PointLoadCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _4042
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PointLoadCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.stability_analyses import _3874
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3997,
        _3945,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PointLoadCompoundStabilityAnalysis")


class PointLoadCompoundStabilityAnalysis(
    _4042.VirtualComponentCompoundStabilityAnalysis
):
    """PointLoadCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PointLoadCompoundStabilityAnalysis")

    class _Cast_PointLoadCompoundStabilityAnalysis:
        """Special nested class for casting PointLoadCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
            parent: "PointLoadCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_stability_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_4042.VirtualComponentCompoundStabilityAnalysis":
            return self._parent._cast(_4042.VirtualComponentCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_3997.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3997,
            )

            return self._parent._cast(_3997.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_3945.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3945,
            )

            return self._parent._cast(_3945.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def point_load_compound_stability_analysis(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
        ) -> "PointLoadCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PointLoadCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_3874.PointLoadStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PointLoadStabilityAnalysis]

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
    ) -> "List[_3874.PointLoadStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PointLoadStabilityAnalysis]

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
    ) -> "PointLoadCompoundStabilityAnalysis._Cast_PointLoadCompoundStabilityAnalysis":
        return self._Cast_PointLoadCompoundStabilityAnalysis(self)
