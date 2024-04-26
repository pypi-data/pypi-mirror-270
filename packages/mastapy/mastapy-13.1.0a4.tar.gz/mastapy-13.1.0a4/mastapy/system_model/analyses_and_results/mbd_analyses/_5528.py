"""StraightBevelSunGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5522
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "StraightBevelSunGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2568
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5419,
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
__all__ = ("StraightBevelSunGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="StraightBevelSunGearMultibodyDynamicsAnalysis")


class StraightBevelSunGearMultibodyDynamicsAnalysis(
    _5522.StraightBevelDiffGearMultibodyDynamicsAnalysis
):
    """StraightBevelSunGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelSunGearMultibodyDynamicsAnalysis"
    )

    class _Cast_StraightBevelSunGearMultibodyDynamicsAnalysis:
        """Special nested class for casting StraightBevelSunGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
            parent: "StraightBevelSunGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5522.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5522.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5419.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.BevelGearMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5404

            return self._parent._cast(
                _5404.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5463.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
        ) -> "StraightBevelSunGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "StraightBevelSunGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2568.StraightBevelSunGear":
        """mastapy.system_model.part_model.gears.StraightBevelSunGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelSunGearMultibodyDynamicsAnalysis._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis":
        return self._Cast_StraightBevelSunGearMultibodyDynamicsAnalysis(self)
