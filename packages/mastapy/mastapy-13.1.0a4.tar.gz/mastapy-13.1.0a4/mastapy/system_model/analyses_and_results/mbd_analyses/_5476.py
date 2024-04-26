"""KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5437
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5475,
        _5474,
        _5479,
        _5482,
        _5464,
        _5513,
        _5399,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis"
)


class KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
    _5437.ConicalGearSetMultibodyDynamicsAnalysis
):
    """KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
            parent: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5437.ConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5437.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5464.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5464

            return self._parent._cast(_5464.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(
                _5479.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> (
            "_5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
        ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2555.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis]

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
    def klingelnberg_cyclo_palloid_conical_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5475.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidConicalGearsMultibodyDynamicsAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5474.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]

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
    def klingelnberg_cyclo_palloid_conical_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5474.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidConicalMeshesMultibodyDynamicsAnalysis
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis(
                self
            )
        )
