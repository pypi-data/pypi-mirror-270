"""GearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.analyses_and_results.system_deflections import _2790
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "GearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _69
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2784,
        _2804,
        _2783,
        _2712,
        _2724,
        _2729,
        _2743,
        _2747,
        _2762,
        _2763,
        _2764,
        _2777,
        _2786,
        _2791,
        _2794,
        _2797,
        _2830,
        _2836,
        _2839,
        _2859,
        _2862,
        _2750,
    )
    from mastapy.math_utility.measured_vectors import _1576
    from mastapy.gears.rating import _367
    from mastapy.system_model.analyses_and_results.power_flows import _4116
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshSystemDeflection",)


Self = TypeVar("Self", bound="GearMeshSystemDeflection")


class GearMeshSystemDeflection(_2790.InterMountableComponentConnectionSystemDeflection):
    """GearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshSystemDeflection")

    class _Cast_GearMeshSystemDeflection:
        """Special nested class for casting GearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
            parent: "GearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2724.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2729.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.BevelGearMeshSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2743.ConceptGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2762.CylindricalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2763.CylindricalGearMeshSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2764.CylindricalGearMeshSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(
                _2764.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2777.FaceGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.FaceGearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2786.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(
                _2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(
                _2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(
                _2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2830.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2839.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearMeshSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2859.WormGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2859,
            )

            return self._parent._cast(_2859.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "_2862.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection",
        ) -> "GearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_mesh_stiffness_along_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CalculatedMeshStiffnessAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def flank_sign(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FlankSign

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_torque_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATorqueLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_a_torque_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATorqueRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTorqueLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_b_torque_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTorqueRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def gear_mesh_contact_status(self: Self) -> "_69.GearMeshContactStatus":
        """mastapy.nodal_analysis.GearMeshContactStatus

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshContactStatus

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.GearMeshContactStatus"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._69", "GearMeshContactStatus"
        )(value)

    @property
    def is_in_contact(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsInContact

        if temp is None:
            return False

        return temp

    @property
    def load_in_loa_from_stiffness_model(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadInLOAFromStiffnessModel

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_possible_mesh_stiffness_along_face_width(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPossibleMeshStiffnessAlongFaceWidth

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPower

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_a_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerGearALeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_a_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerGearARightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_b_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerGearBLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def mesh_power_gear_b_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshPowerGearBRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def moment_about_centre_from_stiffness_model(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MomentAboutCentreFromStiffnessModel

        if temp is None:
            return 0.0

        return temp

    @property
    def node_pair_backlash_on_left_side(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairBacklashOnLeftSide

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_backlash_on_right_side(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairBacklashOnRightSide

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_contact_status(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairContactStatus

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_load_in_loa(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairLoadInLOA

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_load_in_loa_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairLoadInLOALeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_load_in_loa_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairLoadInLOARightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_mesh_stiffness(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairMeshStiffness

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_mesh_stiffness_z_theta(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairMeshStiffnessZTheta

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_mesh_stiffness_theta_z(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairMeshStiffnessThetaZ

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_mesh_stiffness_theta_theta(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairMeshStiffnessThetaTheta

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_separations(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparations

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_separations_left_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparationsLeftFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_separations_right_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparationsRightFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def node_pair_separations_inactive_flank(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodePairSeparationsInactiveFlank

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def number_of_teeth_in_contact(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfTeethInContact

        if temp is None:
            return 0

        return temp

    @property
    def stiffness_kzz(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StiffnessKzz

        if temp is None:
            return 0.0

        return temp

    @property
    def total_contact_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalContactLength

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2331.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a(self: Self) -> "_2784.GearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a_total_mesh_force_in_wcs(
        self: Self,
    ) -> "_1576.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearATotalMeshForceInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_2784.GearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b_total_mesh_force_in_wcs(
        self: Self,
    ) -> "_1576.VectorWithLinearAndAngularComponents":
        """mastapy.math_utility.measured_vectors.VectorWithLinearAndAngularComponents

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearBTotalMeshForceInWCS

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mean_contact_point_in_world_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanContactPointInWorldCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def rating(self: Self) -> "_367.GearMeshRating":
        """mastapy.gears.rating.GearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_separations(self: Self) -> "List[_2804.MeshSeparationsAtFaceWidth]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MeshSeparationsAtFaceWidth]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshSeparations

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_set(self: Self) -> "_2783.GearSetSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.GearSetSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4116.GearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.GearMeshPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshSystemDeflection._Cast_GearMeshSystemDeflection":
        return self._Cast_GearMeshSystemDeflection(self)
