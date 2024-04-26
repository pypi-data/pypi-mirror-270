"""RingPinsCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6778,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "RingPinsCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6661
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6726,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="RingPinsCompoundCriticalSpeedAnalysis")


class RingPinsCompoundCriticalSpeedAnalysis(
    _6778.MountableComponentCompoundCriticalSpeedAnalysis
):
    """RingPinsCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RingPinsCompoundCriticalSpeedAnalysis"
    )

    class _Cast_RingPinsCompoundCriticalSpeedAnalysis:
        """Special nested class for casting RingPinsCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
            parent: "RingPinsCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_6778.MountableComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6778.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_6726.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6726,
            )

            return self._parent._cast(_6726.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def ring_pins_compound_critical_speed_analysis(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
        ) -> "RingPinsCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "RingPinsCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

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
    ) -> "List[_6661.RingPinsCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RingPinsCriticalSpeedAnalysis]

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
    ) -> "List[_6661.RingPinsCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.RingPinsCriticalSpeedAnalysis]

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
    ) -> "RingPinsCompoundCriticalSpeedAnalysis._Cast_RingPinsCompoundCriticalSpeedAnalysis":
        return self._Cast_RingPinsCompoundCriticalSpeedAnalysis(self)
