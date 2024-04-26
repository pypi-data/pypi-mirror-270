"""BevelGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3791
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3804,
        _3802,
        _3798,
        _3888,
        _3897,
        _3900,
        _3918,
        _3819,
        _3847,
        _3886,
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetStabilityAnalysis")


class BevelGearSetStabilityAnalysis(_3791.AGMAGleasonConicalGearSetStabilityAnalysis):
    """BevelGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetStabilityAnalysis")

    class _Cast_BevelGearSetStabilityAnalysis:
        """Special nested class for casting BevelGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
            parent: "BevelGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3791.AGMAGleasonConicalGearSetStabilityAnalysis":
            return self._parent._cast(_3791.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3819.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3847.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3798.BevelDifferentialGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3798,
            )

            return self._parent._cast(_3798.BevelDifferentialGearSetStabilityAnalysis)

        @property
        def spiral_bevel_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3888.SpiralBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.SpiralBevelGearSetStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3897.StraightBevelDiffGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3897,
            )

            return self._parent._cast(_3897.StraightBevelDiffGearSetStabilityAnalysis)

        @property
        def straight_bevel_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3900.StraightBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3900,
            )

            return self._parent._cast(_3900.StraightBevelGearSetStabilityAnalysis)

        @property
        def zerol_bevel_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "_3918.ZerolBevelGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3918,
            )

            return self._parent._cast(_3918.ZerolBevelGearSetStabilityAnalysis)

        @property
        def bevel_gear_set_stability_analysis(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
        ) -> "BevelGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2538.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def agma_gleason_conical_gears_stability_analysis(
        self: Self,
    ) -> "List[_3804.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_gears_stability_analysis(
        self: Self,
    ) -> "List[_3804.BevelGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def agma_gleason_conical_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3802.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AGMAGleasonConicalMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3802.BevelGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelGearSetStabilityAnalysis._Cast_BevelGearSetStabilityAnalysis":
        return self._Cast_BevelGearSetStabilityAnalysis(self)
