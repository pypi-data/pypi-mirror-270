"""ConicalGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ConicalGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5436,
        _5435,
        _5405,
        _5415,
        _5420,
        _5468,
        _5476,
        _5479,
        _5482,
        _5516,
        _5523,
        _5526,
        _5547,
        _5513,
        _5399,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConicalGearSetMultibodyDynamicsAnalysis")


class ConicalGearSetMultibodyDynamicsAnalysis(_5464.GearSetMultibodyDynamicsAnalysis):
    """ConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_ConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting ConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
            parent: "ConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5464.GearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5464.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(
                _5405.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(
                _5415.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5420.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5468.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(
                _5476.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> (
            "_5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(
                _5523.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5526.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5526

            return self._parent._cast(
                _5526.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5547

            return self._parent._cast(_5547.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "ConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2542.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5436.ConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5436.ConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5435.ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5435.ConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConicalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalGearSetMultibodyDynamicsAnalysis._Cast_ConicalGearSetMultibodyDynamicsAnalysis":
        return self._Cast_ConicalGearSetMultibodyDynamicsAnalysis(self)
