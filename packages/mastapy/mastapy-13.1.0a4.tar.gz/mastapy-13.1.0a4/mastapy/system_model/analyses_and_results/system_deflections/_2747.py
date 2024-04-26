"""ConicalGearMeshSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2782
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ConicalGearMeshSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1160, _1165, _1170
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2749,
        _2712,
        _2724,
        _2729,
        _2786,
        _2791,
        _2794,
        _2797,
        _2830,
        _2836,
        _2839,
        _2862,
        _2790,
        _2750,
    )
    from mastapy.gears.ltca.conical import _877
    from mastapy.gears.rating.conical import _546
    from mastapy.system_model.analyses_and_results.power_flows import _4087
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshSystemDeflection")


class ConicalGearMeshSystemDeflection(_2782.GearMeshSystemDeflection):
    """ConicalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshSystemDeflection")

    class _Cast_ConicalGearMeshSystemDeflection:
        """Special nested class for casting ConicalGearMeshSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
            parent: "ConicalGearMeshSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2724.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2729.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.BevelGearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2786.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(
                _2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(
                _2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(
                _2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2830.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearMeshSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2839.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "_2862.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
        ) -> "ConicalGearMeshSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_e(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaE

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_sigma(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaSigma

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xp(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaXP

        if temp is None:
            return 0.0

        return temp

    @property
    def delta_xw(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeltaXW

        if temp is None:
            return 0.0

        return temp

    @property
    def include_mesh_node_misalignments_in_default_report(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport

        if temp is None:
            return False

        return temp

    @property
    def linear_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def load_in_line_of_action_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadInLineOfActionFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def loaded_flank(self: Self) -> "_1160.ActiveConicalFlank":
        """mastapy.gears.gear_designs.conical.ActiveConicalFlank

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedFlank

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.ActiveConicalFlank"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1160", "ActiveConicalFlank"
        )(value)

    @property
    def pinion_angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_torque_for_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionTorqueForLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_force_in_line_of_action_at_mesh_node(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearADueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_a_due_to_moment_at_mesh_node(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearADueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_force_in_line_of_action_at_mesh_node(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearBDueToForceInLineOfActionAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def torque_on_gear_b_due_to_moment_at_mesh_node(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TorqueOnGearBDueToMomentAtMeshNode

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_angular_misalignment_in_surface_of_action(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelAngularMisalignmentInSurfaceOfAction

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2325.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_a(self: Self) -> "_2749.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_2749.ConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConicalGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def ltca_results(self: Self) -> "_877.ConicalMeshLoadDistributionAnalysis":
        """mastapy.gears.ltca.conical.ConicalMeshLoadDistributionAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_design(self: Self) -> "_1165.ConicalGearMeshDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_pinion(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_total(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mesh_node_misalignments_wheel(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshNodeMisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_pinion(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsPinion

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_total(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsTotal

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_wheel(self: Self) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentsWheel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_pinion(
        self: Self,
    ) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodePinion
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_total(
        self: Self,
    ) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeTotal
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignments_with_respect_to_cross_point_using_reference_fe_substructure_node_wheel(
        self: Self,
    ) -> "_1170.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.MisalignmentsWithRespectToCrossPointUsingReferenceFESubstructureNodeWheel
        )

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_546.ConicalGearMeshRating":
        """mastapy.gears.rating.conical.ConicalGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4087.ConicalGearMeshPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ConicalGearMeshPowerFlow

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
    ) -> "ConicalGearMeshSystemDeflection._Cast_ConicalGearMeshSystemDeflection":
        return self._Cast_ConicalGearMeshSystemDeflection(self)
