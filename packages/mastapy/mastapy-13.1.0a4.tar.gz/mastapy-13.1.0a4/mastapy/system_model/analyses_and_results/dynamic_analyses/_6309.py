"""AGMAGleasonConicalGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "AGMAGleasonConicalGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2532
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6307,
        _6308,
        _6316,
        _6321,
        _6369,
        _6406,
        _6412,
        _6415,
        _6433,
        _6365,
        _6403,
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
__all__ = ("AGMAGleasonConicalGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetDynamicAnalysis")


class AGMAGleasonConicalGearSetDynamicAnalysis(_6337.ConicalGearSetDynamicAnalysis):
    """AGMAGleasonConicalGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetDynamicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetDynamicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
            parent: "AGMAGleasonConicalGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6337.ConicalGearSetDynamicAnalysis":
            return self._parent._cast(_6337.ConicalGearSetDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6365.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6316.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316

            return self._parent._cast(_6316.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6321.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.BevelGearSetDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6369.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.HypoidGearSetDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6406.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.SpiralBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6412.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6412

            return self._parent._cast(_6412.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6415.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6415

            return self._parent._cast(_6415.StraightBevelGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "_6433.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6433

            return self._parent._cast(_6433.ZerolBevelGearSetDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
        ) -> "AGMAGleasonConicalGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2532.AGMAGleasonConicalGearSet":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def conical_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6307.AGMAGleasonConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6307.AGMAGleasonConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def conical_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6308.AGMAGleasonConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6308.AGMAGleasonConicalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.AGMAGleasonConicalGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetDynamicAnalysis._Cast_AGMAGleasonConicalGearSetDynamicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetDynamicAnalysis(self)
