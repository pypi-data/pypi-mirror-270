"""RingPinsCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6511
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "RingPinsCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2588
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6459,
        _6513,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="RingPinsCompoundDynamicAnalysis")


class RingPinsCompoundDynamicAnalysis(_6511.MountableComponentCompoundDynamicAnalysis):
    """RingPinsCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsCompoundDynamicAnalysis")

    class _Cast_RingPinsCompoundDynamicAnalysis:
        """Special nested class for casting RingPinsCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
            parent: "RingPinsCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_6511.MountableComponentCompoundDynamicAnalysis":
            return self._parent._cast(_6511.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_6459.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6459,
            )

            return self._parent._cast(_6459.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_6513.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6513,
            )

            return self._parent._cast(_6513.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def ring_pins_compound_dynamic_analysis(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
        ) -> "RingPinsCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsCompoundDynamicAnalysis.TYPE"):
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
    ) -> "List[_6394.RingPinsDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsDynamicAnalysis]

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
    def component_analysis_cases(self: Self) -> "List[_6394.RingPinsDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.RingPinsDynamicAnalysis]

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
    ) -> "RingPinsCompoundDynamicAnalysis._Cast_RingPinsCompoundDynamicAnalysis":
        return self._Cast_RingPinsCompoundDynamicAnalysis(self)
