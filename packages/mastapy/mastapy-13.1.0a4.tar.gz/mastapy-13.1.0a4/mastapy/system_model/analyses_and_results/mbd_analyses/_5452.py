"""CylindricalGearSetMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CylindricalGearSetMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.static_loads import _6892
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5451,
        _5450,
        _5496,
        _5513,
        _5399,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetMultibodyDynamicsAnalysis")


class CylindricalGearSetMultibodyDynamicsAnalysis(
    _5464.GearSetMultibodyDynamicsAnalysis
):
    """CylindricalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetMultibodyDynamicsAnalysis"
    )

    class _Cast_CylindricalGearSetMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalGearSetMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
            parent: "CylindricalGearSetMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5464.GearSetMultibodyDynamicsAnalysis":
            return self._parent._cast(_5464.GearSetMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "_5496.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
        ) -> "CylindricalGearSetMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6892.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5451.CylindricalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis]

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
    def cylindrical_gears_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5451.CylindricalGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5450.CylindricalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMeshMultibodyDynamicsAnalysis]

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
    def cylindrical_meshes_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5450.CylindricalGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetMultibodyDynamicsAnalysis._Cast_CylindricalGearSetMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalGearSetMultibodyDynamicsAnalysis(self)
