"""GearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6363,
        _6364,
        _6309,
        _6316,
        _6321,
        _6334,
        _6337,
        _6352,
        _6360,
        _6369,
        _6373,
        _6376,
        _6379,
        _6389,
        _6406,
        _6412,
        _6415,
        _6430,
        _6433,
        _6303,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="GearSetDynamicAnalysis")


class GearSetDynamicAnalysis(_6403.SpecialisedAssemblyDynamicAnalysis):
    """GearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDynamicAnalysis")

    class _Cast_GearSetDynamicAnalysis:
        """Special nested class for casting GearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
            parent: "GearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6309.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6316.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6321.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.BevelGearSetDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6334.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6352.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(_6352.CylindricalGearSetDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6360.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.FaceGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6369.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6373

            return self._parent._cast(
                _6373.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(
                _6376.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(
                _6379.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6389.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.PlanetaryGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6406.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6412.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6415.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.StraightBevelGearSetDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6430.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6430

            return self._parent._cast(_6430.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "_6433.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6433

            return self._parent._cast(_6433.ZerolBevelGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis",
        ) -> "GearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2550.GearSet":
        """mastapy.system_model.part_model.gears.GearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_dynamic_analysis(self: Self) -> "List[_6363.GearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_dynamic_analysis(self: Self) -> "List[_6364.GearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.GearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearSetDynamicAnalysis._Cast_GearSetDynamicAnalysis":
        return self._Cast_GearSetDynamicAnalysis(self)
