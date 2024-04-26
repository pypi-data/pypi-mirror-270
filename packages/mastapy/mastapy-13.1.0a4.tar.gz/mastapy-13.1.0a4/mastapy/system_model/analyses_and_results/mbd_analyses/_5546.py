"""ZerolBevelGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5419
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ZerolBevelGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _7012
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5404,
        _5436,
        _5463,
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMultibodyDynamicsAnalysis")


class ZerolBevelGearMultibodyDynamicsAnalysis(_5419.BevelGearMultibodyDynamicsAnalysis):
    """ZerolBevelGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMultibodyDynamicsAnalysis"
    )

    class _Cast_ZerolBevelGearMultibodyDynamicsAnalysis:
        """Special nested class for casting ZerolBevelGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
            parent: "ZerolBevelGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5419.BevelGearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5419.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5463.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
        ) -> "ZerolBevelGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_7012.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

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
    ) -> "ZerolBevelGearMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMultibodyDynamicsAnalysis":
        return self._Cast_ZerolBevelGearMultibodyDynamicsAnalysis(self)
