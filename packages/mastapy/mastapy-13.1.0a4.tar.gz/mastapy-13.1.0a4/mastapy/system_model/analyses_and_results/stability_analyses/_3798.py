"""BevelDifferentialGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelDifferentialGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3799,
        _3797,
        _3791,
        _3819,
        _3847,
        _3886,
        _3786,
        _3867,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetStabilityAnalysis")


class BevelDifferentialGearSetStabilityAnalysis(_3803.BevelGearSetStabilityAnalysis):
    """BevelDifferentialGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetStabilityAnalysis"
    )

    class _Cast_BevelDifferentialGearSetStabilityAnalysis:
        """Special nested class for casting BevelDifferentialGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
            parent: "BevelDifferentialGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3803.BevelGearSetStabilityAnalysis":
            return self._parent._cast(_3803.BevelGearSetStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_set_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3791.AGMAGleasonConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3791,
            )

            return self._parent._cast(_3791.AGMAGleasonConicalGearSetStabilityAnalysis)

        @property
        def conical_gear_set_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3819.ConicalGearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ConicalGearSetStabilityAnalysis)

        @property
        def gear_set_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3847.GearSetStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3847,
            )

            return self._parent._cast(_3847.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3886.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3886,
            )

            return self._parent._cast(_3886.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3786.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3786,
            )

            return self._parent._cast(_3786.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_3867.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3867,
            )

            return self._parent._cast(_3867.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_stability_analysis(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
        ) -> "BevelDifferentialGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6851.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_stability_analysis(
        self: Self,
    ) -> "List[_3799.BevelDifferentialGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearStabilityAnalysis]

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
    def bevel_differential_gears_stability_analysis(
        self: Self,
    ) -> "List[_3799.BevelDifferentialGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3797.BevelDifferentialGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearMeshStabilityAnalysis]

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
    def bevel_differential_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3797.BevelDifferentialGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetStabilityAnalysis._Cast_BevelDifferentialGearSetStabilityAnalysis":
        return self._Cast_BevelDifferentialGearSetStabilityAnalysis(self)
