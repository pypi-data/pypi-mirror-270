"""PulleyMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PULLEY_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PulleyMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.static_loads import _6967
    from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5551
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5445,
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PulleyMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PulleyMultibodyDynamicsAnalysis")


class PulleyMultibodyDynamicsAnalysis(_5441.CouplingHalfMultibodyDynamicsAnalysis):
    """PulleyMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PULLEY_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PulleyMultibodyDynamicsAnalysis")

    class _Cast_PulleyMultibodyDynamicsAnalysis:
        """Special nested class for casting PulleyMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
            parent: "PulleyMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "_5445.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
        ) -> "PulleyMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PulleyMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_on_pulley_from_belts(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ForceOnPulleyFromBelts

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def pulley_torque(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PulleyTorque

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2610.Pulley":
        """mastapy.system_model.part_model.couplings.Pulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6967.PulleyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PulleyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def peak_pulley_torque(self: Self) -> "List[_5551.DynamicTorqueResultAtTime]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.reporting.DynamicTorqueResultAtTime]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakPulleyTorque

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PulleyMultibodyDynamicsAnalysis._Cast_PulleyMultibodyDynamicsAnalysis":
        return self._Cast_PulleyMultibodyDynamicsAnalysis(self)
