"""FEPartCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6703,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "FEPartCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6628
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6726,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundCriticalSpeedAnalysis")


class FEPartCompoundCriticalSpeedAnalysis(
    _6703.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
):
    """FEPartCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundCriticalSpeedAnalysis")

    class _Cast_FEPartCompoundCriticalSpeedAnalysis:
        """Special nested class for casting FEPartCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
            parent: "FEPartCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6703.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6703.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def fe_part_compound_critical_speed_analysis(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
        ) -> "FEPartCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "FEPartCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.FEPart":
        """mastapy.system_model.part_model.FEPart

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
    ) -> "List[_6628.FEPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FEPartCriticalSpeedAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.compound.FEPartCompoundCriticalSpeedAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6628.FEPartCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.FEPartCriticalSpeedAnalysis]

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
    ) -> (
        "FEPartCompoundCriticalSpeedAnalysis._Cast_FEPartCompoundCriticalSpeedAnalysis"
    ):
        return self._Cast_FEPartCompoundCriticalSpeedAnalysis(self)
