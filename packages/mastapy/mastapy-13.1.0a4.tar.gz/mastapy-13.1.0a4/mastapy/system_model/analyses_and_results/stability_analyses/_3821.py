"""ConnectionStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ConnectionStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2290
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3893,
        _3789,
        _3790,
        _3795,
        _3797,
        _3802,
        _3807,
        _3810,
        _3812,
        _3815,
        _3818,
        _3823,
        _3827,
        _3831,
        _3832,
        _3834,
        _3841,
        _3846,
        _3850,
        _3853,
        _3854,
        _3857,
        _3860,
        _3868,
        _3871,
        _3878,
        _3880,
        _3885,
        _3887,
        _3890,
        _3896,
        _3899,
        _3908,
        _3914,
        _3917,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectionStabilityAnalysis")


class ConnectionStabilityAnalysis(_7567.ConnectionStaticLoadAnalysisCase):
    """ConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionStabilityAnalysis")

    class _Cast_ConnectionStabilityAnalysis:
        """Special nested class for casting ConnectionStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
            parent: "ConnectionStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_static_load_analysis_case(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3789.AbstractShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3789,
            )

            return self._parent._cast(
                _3789.AbstractShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3790.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def belt_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3795.BeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3795,
            )

            return self._parent._cast(_3795.BeltConnectionStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3797.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3802.BevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3802,
            )

            return self._parent._cast(_3802.BevelGearMeshStabilityAnalysis)

        @property
        def clutch_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3807.ClutchConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.ClutchConnectionStabilityAnalysis)

        @property
        def coaxial_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3810.CoaxialConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3810,
            )

            return self._parent._cast(_3810.CoaxialConnectionStabilityAnalysis)

        @property
        def concept_coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3812.ConceptCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.ConceptCouplingConnectionStabilityAnalysis)

        @property
        def concept_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3815.ConceptGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.ConceptGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3818.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3818,
            )

            return self._parent._cast(_3818.ConicalGearMeshStabilityAnalysis)

        @property
        def coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3823.CouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.CouplingConnectionStabilityAnalysis)

        @property
        def cvt_belt_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3827.CVTBeltConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.CVTBeltConnectionStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3831.CycloidalDiscCentralBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(
                _3831.CycloidalDiscCentralBearingConnectionStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3832.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.CycloidalDiscPlanetaryBearingConnectionStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3834.CylindricalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3834,
            )

            return self._parent._cast(_3834.CylindricalGearMeshStabilityAnalysis)

        @property
        def face_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3841.FaceGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(_3841.FaceGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3846.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.GearMeshStabilityAnalysis)

        @property
        def hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3850.HypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3850,
            )

            return self._parent._cast(_3850.HypoidGearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3853.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(
                _3853.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3854.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(
                _3854.KlingelnbergCycloPalloidConicalGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3857.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3857,
            )

            return self._parent._cast(
                _3857.KlingelnbergCycloPalloidHypoidGearMeshStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3860.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(
                _3860.KlingelnbergCycloPalloidSpiralBevelGearMeshStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3868.PartToPartShearCouplingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(
                _3868.PartToPartShearCouplingConnectionStabilityAnalysis
            )

        @property
        def planetary_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3871.PlanetaryConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.PlanetaryConnectionStabilityAnalysis)

        @property
        def ring_pins_to_disc_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3878.RingPinsToDiscConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.RingPinsToDiscConnectionStabilityAnalysis)

        @property
        def rolling_ring_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3880.RollingRingConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.RollingRingConnectionStabilityAnalysis)

        @property
        def shaft_to_mountable_component_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3885.ShaftToMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(
                _3885.ShaftToMountableComponentConnectionStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3887.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3887,
            )

            return self._parent._cast(_3887.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def spring_damper_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3890.SpringDamperConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.SpringDamperConnectionStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3896.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3899.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3899,
            )

            return self._parent._cast(_3899.StraightBevelGearMeshStabilityAnalysis)

        @property
        def torque_converter_connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3908.TorqueConverterConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3908,
            )

            return self._parent._cast(_3908.TorqueConverterConnectionStabilityAnalysis)

        @property
        def worm_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3914.WormGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3914,
            )

            return self._parent._cast(_3914.WormGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "_3917.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3917,
            )

            return self._parent._cast(_3917.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def connection_stability_analysis(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
        ) -> "ConnectionStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConnectionStabilityAnalysis.TYPE"):
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
    def stability_analysis(self: Self) -> "_3893.StabilityAnalysis":
        """mastapy.system_model.analyses_and_results.stability_analyses.StabilityAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StabilityAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionStabilityAnalysis._Cast_ConnectionStabilityAnalysis":
        return self._Cast_ConnectionStabilityAnalysis(self)
