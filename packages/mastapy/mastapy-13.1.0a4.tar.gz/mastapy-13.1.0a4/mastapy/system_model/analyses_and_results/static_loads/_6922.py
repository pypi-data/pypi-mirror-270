"""GearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion, overridable_enum_runtime
from mastapy._internal.implicit import overridable
from mastapy.system_model.analyses_and_results.static_loads import _6950, _6979
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5462
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7039,
    )
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6917,
        _6919,
        _6842,
        _6851,
        _6856,
        _6870,
        _6875,
        _6892,
        _6913,
        _6934,
        _6941,
        _6944,
        _6947,
        _6960,
        _6982,
        _6988,
        _6991,
        _7011,
        _7014,
        _6833,
        _6955,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadCase",)


Self = TypeVar("Self", bound="GearSetLoadCase")


class GearSetLoadCase(_6979.SpecialisedAssemblyLoadCase):
    """GearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadCase")

    class _Cast_GearSetLoadCase:
        """Special nested class for casting GearSetLoadCase to subclasses."""

        def __init__(
            self: "GearSetLoadCase._Cast_GearSetLoadCase", parent: "GearSetLoadCase"
        ):
            self._parent = parent

        @property
        def specialised_assembly_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6979.SpecialisedAssemblyLoadCase":
            return self._parent._cast(_6979.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6833.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6955.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.PartLoadCase)

        @property
        def part_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6842.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6851.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6856.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.BevelGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6870.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6870

            return self._parent._cast(_6870.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6875.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6875

            return self._parent._cast(_6875.ConicalGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6892.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6892

            return self._parent._cast(_6892.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6913.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6913

            return self._parent._cast(_6913.FaceGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6934.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6941.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(
                _6941.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6944

            return self._parent._cast(
                _6944.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(
                _6947.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def planetary_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6960.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.PlanetaryGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6982.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6982

            return self._parent._cast(_6982.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6988.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_6991.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6991

            return self._parent._cast(_6991.StraightBevelGearSetLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_7011.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7011

            return self._parent._cast(_7011.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "_7014.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7014

            return self._parent._cast(_7014.ZerolBevelGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "GearSetLoadCase._Cast_GearSetLoadCase",
        ) -> "GearSetLoadCase":
            return self._parent

        def __getattr__(self: "GearSetLoadCase._Cast_GearSetLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_data_is_up_to_date(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitationDataIsUpToDate

        if temp is None:
            return False

        return temp

    @property
    def gear_mesh_stiffness_model(self: Self) -> "_5462.GearMeshStiffnessModel":
        """mastapy.system_model.analyses_and_results.mbd_analyses.GearMeshStiffnessModel"""
        temp = self.wrapped.GearMeshStiffnessModel

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model.analyses_and_results.mbd_analyses._5462",
            "GearMeshStiffnessModel",
        )(value)

    @gear_mesh_stiffness_model.setter
    @enforce_parameter_types
    def gear_mesh_stiffness_model(self: Self, value: "_5462.GearMeshStiffnessModel"):
        value = conversion.mp_to_pn_enum(
            value,
            "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.GearMeshStiffnessModel",
        )
        self.wrapped.GearMeshStiffnessModel = value

    @property
    def mesh_stiffness_source(
        self: Self,
    ) -> "overridable.Overridable_MeshStiffnessSource":
        """Overridable[mastapy.system_model.analyses_and_results.static_loads.MeshStiffnessSource]"""
        temp = self.wrapped.MeshStiffnessSource

        if temp is None:
            return None

        value = overridable.Overridable_MeshStiffnessSource.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @mesh_stiffness_source.setter
    @enforce_parameter_types
    def mesh_stiffness_source(
        self: Self,
        value: "Union[_6950.MeshStiffnessSource, Tuple[_6950.MeshStiffnessSource, bool]]",
    ):
        wrapper_type = overridable.Overridable_MeshStiffnessSource.wrapper_type()
        enclosed_type = overridable.Overridable_MeshStiffnessSource.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.MeshStiffnessSource = value

    @property
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self,
    ) -> "bool":
        """bool"""
        temp = self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation

        if temp is None:
            return False

        return temp

    @use_advanced_model_in_advanced_time_stepping_analysis_for_modulation.setter
    @enforce_parameter_types
    def use_advanced_model_in_advanced_time_stepping_analysis_for_modulation(
        self: Self, value: "bool"
    ):
        self.wrapped.UseAdvancedModelInAdvancedTimeSteppingAnalysisForModulation = (
            bool(value) if value is not None else False
        )

    @property
    def advanced_time_stepping_analysis_for_modulation_options(
        self: Self,
    ) -> "_7039.AdvancedTimeSteppingAnalysisForModulationOptions":
        """mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AdvancedTimeSteppingAnalysisForModulationOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AdvancedTimeSteppingAnalysisForModulationOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def gears_load_case(self: Self) -> "List[_6917.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gears_without_clones(self: Self) -> "List[_6917.GearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsWithoutClones

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_load_case(self: Self) -> "List[_6919.GearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_without_planetary_duplicates(
        self: Self,
    ) -> "List[_6919.GearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.GearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesWithoutPlanetaryDuplicates

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "GearSetLoadCase._Cast_GearSetLoadCase":
        return self._Cast_GearSetLoadCase(self)
