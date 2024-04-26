"""SynchroniserHalfCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6687
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SynchroniserHalfCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.static_loads import _6994
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6608,
        _6649,
        _6594,
        _6651,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCriticalSpeedAnalysis")


class SynchroniserHalfCriticalSpeedAnalysis(
    _6687.SynchroniserPartCriticalSpeedAnalysis
):
    """SynchroniserHalfCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCriticalSpeedAnalysis"
    )

    class _Cast_SynchroniserHalfCriticalSpeedAnalysis:
        """Special nested class for casting SynchroniserHalfCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
            parent: "SynchroniserHalfCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_6687.SynchroniserPartCriticalSpeedAnalysis":
            return self._parent._cast(_6687.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_6608.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6608,
            )

            return self._parent._cast(_6608.CouplingHalfCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_6649.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6649,
            )

            return self._parent._cast(_6649.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_6594.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6594,
            )

            return self._parent._cast(_6594.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_6651.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6651,
            )

            return self._parent._cast(_6651.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
        ) -> "SynchroniserHalfCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserHalfCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6994.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfCriticalSpeedAnalysis._Cast_SynchroniserHalfCriticalSpeedAnalysis":
        return self._Cast_SynchroniserHalfCriticalSpeedAnalysis(self)
