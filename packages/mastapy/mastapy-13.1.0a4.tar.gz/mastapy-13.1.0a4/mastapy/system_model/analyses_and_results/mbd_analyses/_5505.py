"""RollingRingMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "RollingRingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.static_loads import _6974
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RollingRingMultibodyDynamicsAnalysis")


class RollingRingMultibodyDynamicsAnalysis(_5441.CouplingHalfMultibodyDynamicsAnalysis):
    """RollingRingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingMultibodyDynamicsAnalysis")

    class _Cast_RollingRingMultibodyDynamicsAnalysis:
        """Special nested class for casting RollingRingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
            parent: "RollingRingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
        ) -> "RollingRingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6974.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RollingRingMultibodyDynamicsAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "RollingRingMultibodyDynamicsAnalysis._Cast_RollingRingMultibodyDynamicsAnalysis":
        return self._Cast_RollingRingMultibodyDynamicsAnalysis(self)
