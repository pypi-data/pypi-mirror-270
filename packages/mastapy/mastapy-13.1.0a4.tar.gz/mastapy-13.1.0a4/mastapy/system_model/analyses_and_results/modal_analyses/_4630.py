"""ConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4677,
        _4598,
        _4599,
        _4604,
        _4606,
        _4611,
        _4616,
        _4619,
        _4621,
        _4624,
        _4627,
        _4633,
        _4636,
        _4640,
        _4642,
        _4643,
        _4652,
        _4658,
        _4662,
        _4665,
        _4666,
        _4669,
        _4672,
        _4686,
        _4689,
        _4696,
        _4698,
        _4704,
        _4706,
        _4709,
        _4712,
        _4715,
        _4724,
        _4733,
        _4736,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4749
    from mastapy.system_model.analyses_and_results.system_deflections import _2750
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionModalAnalysis",)


Self = TypeVar("Self", bound="ConnectionModalAnalysis")


class ConnectionModalAnalysis(_7567.ConnectionStaticLoadAnalysisCase):
    """ConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionModalAnalysis")

    class _Cast_ConnectionModalAnalysis:
        """Special nested class for casting ConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
            parent: "ConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4598.AbstractShaftToMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(
                _4598.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4599.AGMAGleasonConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.AGMAGleasonConicalGearMeshModalAnalysis)

        @property
        def belt_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4604.BeltConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.BeltConnectionModalAnalysis)

        @property
        def bevel_differential_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4606.BevelDifferentialGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4606

            return self._parent._cast(_4606.BevelDifferentialGearMeshModalAnalysis)

        @property
        def bevel_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4611.BevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4611

            return self._parent._cast(_4611.BevelGearMeshModalAnalysis)

        @property
        def clutch_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4616.ClutchConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.ClutchConnectionModalAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4619.CoaxialConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(_4619.CoaxialConnectionModalAnalysis)

        @property
        def concept_coupling_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4621.ConceptCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4621

            return self._parent._cast(_4621.ConceptCouplingConnectionModalAnalysis)

        @property
        def concept_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4624.ConceptGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.ConceptGearMeshModalAnalysis)

        @property
        def conical_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4627.ConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4627

            return self._parent._cast(_4627.ConicalGearMeshModalAnalysis)

        @property
        def coupling_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4633.CouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.CouplingConnectionModalAnalysis)

        @property
        def cvt_belt_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4636.CVTBeltConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4636

            return self._parent._cast(_4636.CVTBeltConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4640.CycloidalDiscCentralBearingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(
                _4640.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4642.CycloidalDiscPlanetaryBearingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(
                _4642.CycloidalDiscPlanetaryBearingConnectionModalAnalysis
            )

        @property
        def cylindrical_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4643.CylindricalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.CylindricalGearMeshModalAnalysis)

        @property
        def face_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4652.FaceGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(_4652.FaceGearMeshModalAnalysis)

        @property
        def gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4658.GearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4658

            return self._parent._cast(_4658.GearMeshModalAnalysis)

        @property
        def hypoid_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4662.HypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.HypoidGearMeshModalAnalysis)

        @property
        def inter_mountable_component_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4665.InterMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4665

            return self._parent._cast(
                _4665.InterMountableComponentConnectionModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(
                _4666.KlingelnbergCycloPalloidConicalGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4669.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(
                _4669.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4672.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(
                _4672.KlingelnbergCycloPalloidSpiralBevelGearMeshModalAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4686.PartToPartShearCouplingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(
                _4686.PartToPartShearCouplingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4689.PlanetaryConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.PlanetaryConnectionModalAnalysis)

        @property
        def ring_pins_to_disc_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4696.RingPinsToDiscConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.RingPinsToDiscConnectionModalAnalysis)

        @property
        def rolling_ring_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4698.RollingRingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.RollingRingConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4704.ShaftToMountableComponentConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(
                _4704.ShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4706.SpiralBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.SpiralBevelGearMeshModalAnalysis)

        @property
        def spring_damper_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4709.SpringDamperConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4709

            return self._parent._cast(_4709.SpringDamperConnectionModalAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4712.StraightBevelDiffGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4712

            return self._parent._cast(_4712.StraightBevelDiffGearMeshModalAnalysis)

        @property
        def straight_bevel_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4715.StraightBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4715

            return self._parent._cast(_4715.StraightBevelGearMeshModalAnalysis)

        @property
        def torque_converter_connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4724.TorqueConverterConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4724

            return self._parent._cast(_4724.TorqueConverterConnectionModalAnalysis)

        @property
        def worm_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4733.WormGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4733

            return self._parent._cast(_4733.WormGearMeshModalAnalysis)

        @property
        def zerol_bevel_gear_mesh_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "_4736.ZerolBevelGearMeshModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4736

            return self._parent._cast(_4736.ZerolBevelGearMeshModalAnalysis)

        @property
        def connection_modal_analysis(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis",
        ) -> "ConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2290.Connection":
        """mastapy.system_model.connections_and_sockets.Connection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis(self: Self) -> "_4677.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: Self,
    ) -> "List[_4749.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2750.ConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ConnectionModalAnalysis._Cast_ConnectionModalAnalysis":
        return self._Cast_ConnectionModalAnalysis(self)
