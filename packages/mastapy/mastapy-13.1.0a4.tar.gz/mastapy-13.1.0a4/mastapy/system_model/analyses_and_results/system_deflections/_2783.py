"""GearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.system_model.analyses_and_results.system_deflections import _2829
from mastapy._internal.cast_exception import CastException

_GEAR_SET_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationDetail"
)
_GEAR_SET_MODES = python_net_import("SMT.MastaAPI.Gears", "GearSetModes")
_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_BOOLEAN = python_net_import("System", "Boolean")
_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.gears.rating import _370
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2784,
        _2782,
        _2713,
        _2725,
        _2730,
        _2744,
        _2748,
        _2765,
        _2766,
        _2767,
        _2778,
        _2787,
        _2792,
        _2795,
        _2798,
        _2831,
        _2837,
        _2840,
        _2860,
        _2863,
        _2708,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.power_flows import _4118
    from mastapy.gears.analysis import _1241, _1238
    from mastapy.gears import _336
    from mastapy import _7585
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetSystemDeflection",)


Self = TypeVar("Self", bound="GearSetSystemDeflection")


class GearSetSystemDeflection(_2829.SpecialisedAssemblySystemDeflection):
    """GearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetSystemDeflection")

    class _Cast_GearSetSystemDeflection:
        """Special nested class for casting GearSetSystemDeflection to subclasses."""

        def __init__(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
            parent: "GearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2713.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2713,
            )

            return self._parent._cast(_2713.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2725.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2725,
            )

            return self._parent._cast(_2725.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2730.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.BevelGearSetSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2744.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.ConceptGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2748.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.ConicalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2765.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2765,
            )

            return self._parent._cast(_2765.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2766.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2767.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(
                _2767.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2778.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(_2778.FaceGearSetSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2787.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.HypoidGearSetSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(
                _2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(
                _2795.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2798,
            )

            return self._parent._cast(
                _2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2831.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.SpiralBevelGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2837.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2840.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.StraightBevelGearSetSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2860.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2860,
            )

            return self._parent._cast(_2860.WormGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "_2863.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2863,
            )

            return self._parent._cast(_2863.ZerolBevelGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection",
        ) -> "GearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearSetSystemDeflection._Cast_GearSetSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetSystemDeflection.TYPE"):
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
    def rating(self: Self) -> "_370.GearSetRating":
        """mastapy.gears.rating.GearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_system_deflection(self: Self) -> "List[_2784.GearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_system_deflection(self: Self) -> "List[_2782.GearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.GearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4118.GearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @enforce_parameter_types
    def analysis_for(
        self: Self,
        gear_set_imp_detail: "_1241.GearSetImplementationDetail",
        gear_set_mode: "_336.GearSetModes",
    ) -> "_1238.GearSetImplementationAnalysis":
        """mastapy.gears.analysis.GearSetImplementationAnalysis

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.AnalysisFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @enforce_parameter_types
    def implementation_detail_results_failed_for(
        self: Self,
        gear_set_imp_detail: "_1241.GearSetImplementationDetail",
        gear_set_mode: "_336.GearSetModes",
    ) -> "bool":
        """bool

        Args:
            gear_set_imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        method_result = self.wrapped.ImplementationDetailResultsFailedFor(
            gear_set_imp_detail.wrapped if gear_set_imp_detail else None, gear_set_mode
        )
        return method_result

    @enforce_parameter_types
    def perform_implementation_detail_analysis_with_progress(
        self: Self,
        imp_detail: "_1241.GearSetImplementationDetail",
        gear_set_mode: "_336.GearSetModes",
        progress: "_7585.TaskProgress",
        run_all_planetary_meshes: "bool" = True,
    ):
        """Method does not return.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            progress (mastapy.TaskProgress)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _TASK_PROGRESS, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            progress.wrapped if progress else None,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @enforce_parameter_types
    def perform_implementation_detail_analysis(
        self: Self,
        imp_detail: "_1241.GearSetImplementationDetail",
        gear_set_mode: "_336.GearSetModes",
        run_all_planetary_meshes: "bool" = True,
    ):
        """Method does not return.

        Args:
            imp_detail (mastapy.gears.analysis.GearSetImplementationDetail)
            gear_set_mode (mastapy.gears.GearSetModes)
            run_all_planetary_meshes (bool, optional)
        """
        gear_set_mode = conversion.mp_to_pn_enum(
            gear_set_mode, "SMT.MastaAPI.Gears.GearSetModes"
        )
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformImplementationDetailAnalysis.Overloads[
            _GEAR_SET_IMPLEMENTATION_DETAIL, _GEAR_SET_MODES, _BOOLEAN
        ](
            imp_detail.wrapped if imp_detail else None,
            gear_set_mode,
            run_all_planetary_meshes if run_all_planetary_meshes else False,
        )

    @property
    def cast_to(self: Self) -> "GearSetSystemDeflection._Cast_GearSetSystemDeflection":
        return self._Cast_GearSetSystemDeflection(self)
