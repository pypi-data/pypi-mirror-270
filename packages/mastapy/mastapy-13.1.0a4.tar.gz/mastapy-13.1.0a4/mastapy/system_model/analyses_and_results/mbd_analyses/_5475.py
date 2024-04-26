"""KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5436
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2554
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5478,
        _5481,
        _5463,
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis(
    _5436.ConicalGearMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5436.ConicalGearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5436.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5463.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5463

            return self._parent._cast(_5463.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(
                _5478.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "_5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(
                _5481.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2554.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

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
    ) -> "KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
        return self._Cast_KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis(
            self
        )
