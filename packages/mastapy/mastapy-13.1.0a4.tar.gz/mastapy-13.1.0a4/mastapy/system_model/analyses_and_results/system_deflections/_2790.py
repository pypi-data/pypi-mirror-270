"""InterMountableComponentConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2750
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "InterMountableComponentConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.power_flows import _4123
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2712,
        _2722,
        _2724,
        _2729,
        _2734,
        _2740,
        _2743,
        _2747,
        _2752,
        _2755,
        _2762,
        _2763,
        _2764,
        _2777,
        _2782,
        _2786,
        _2791,
        _2794,
        _2797,
        _2809,
        _2818,
        _2821,
        _2830,
        _2833,
        _2836,
        _2839,
        _2851,
        _2859,
        _2862,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionSystemDeflection",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionSystemDeflection")


class InterMountableComponentConnectionSystemDeflection(
    _2750.ConnectionSystemDeflection
):
    """InterMountableComponentConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionSystemDeflection"
    )

    class _Cast_InterMountableComponentConnectionSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
            parent: "InterMountableComponentConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2712.AGMAGleasonConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.AGMAGleasonConicalGearMeshSystemDeflection)

        @property
        def belt_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2722.BeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2722,
            )

            return self._parent._cast(_2722.BeltConnectionSystemDeflection)

        @property
        def bevel_differential_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2724.BevelDifferentialGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.BevelDifferentialGearMeshSystemDeflection)

        @property
        def bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2729.BevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2729,
            )

            return self._parent._cast(_2729.BevelGearMeshSystemDeflection)

        @property
        def clutch_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2734.ClutchConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2734,
            )

            return self._parent._cast(_2734.ClutchConnectionSystemDeflection)

        @property
        def concept_coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2740.ConceptCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.ConceptCouplingConnectionSystemDeflection)

        @property
        def concept_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2743.ConceptGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2743,
            )

            return self._parent._cast(_2743.ConceptGearMeshSystemDeflection)

        @property
        def conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2747.ConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.ConicalGearMeshSystemDeflection)

        @property
        def coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2752.CouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CouplingConnectionSystemDeflection)

        @property
        def cvt_belt_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2755.CVTBeltConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2755,
            )

            return self._parent._cast(_2755.CVTBeltConnectionSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2762.CylindricalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.CylindricalGearMeshSystemDeflection)

        @property
        def cylindrical_gear_mesh_system_deflection_timestep(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2763.CylindricalGearMeshSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.CylindricalGearMeshSystemDeflectionTimestep)

        @property
        def cylindrical_gear_mesh_system_deflection_with_ltca_results(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2764.CylindricalGearMeshSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(
                _2764.CylindricalGearMeshSystemDeflectionWithLTCAResults
            )

        @property
        def face_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2777.FaceGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(_2777.FaceGearMeshSystemDeflection)

        @property
        def gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2782.GearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.GearMeshSystemDeflection)

        @property
        def hypoid_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2786.HypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.HypoidGearMeshSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2791,
            )

            return self._parent._cast(
                _2791.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(
                _2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2797,
            )

            return self._parent._cast(
                _2797.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2809.PartToPartShearCouplingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2809,
            )

            return self._parent._cast(
                _2809.PartToPartShearCouplingConnectionSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2818.RingPinsToDiscConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2818,
            )

            return self._parent._cast(_2818.RingPinsToDiscConnectionSystemDeflection)

        @property
        def rolling_ring_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2821.RollingRingConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.RollingRingConnectionSystemDeflection)

        @property
        def spiral_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2830.SpiralBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2830,
            )

            return self._parent._cast(_2830.SpiralBevelGearMeshSystemDeflection)

        @property
        def spring_damper_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2833.SpringDamperConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.SpringDamperConnectionSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2836.StraightBevelDiffGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.StraightBevelDiffGearMeshSystemDeflection)

        @property
        def straight_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2839.StraightBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.StraightBevelGearMeshSystemDeflection)

        @property
        def torque_converter_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2851.TorqueConverterConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2851,
            )

            return self._parent._cast(_2851.TorqueConverterConnectionSystemDeflection)

        @property
        def worm_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2859.WormGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2859,
            )

            return self._parent._cast(_2859.WormGearMeshSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "_2862.ZerolBevelGearMeshSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2862,
            )

            return self._parent._cast(_2862.ZerolBevelGearMeshSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
        ) -> "InterMountableComponentConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection",
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
        self: Self,
        instance_to_wrap: "InterMountableComponentConnectionSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4123.InterMountableComponentConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.InterMountableComponentConnectionPowerFlow

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
    ) -> "InterMountableComponentConnectionSystemDeflection._Cast_InterMountableComponentConnectionSystemDeflection":
        return self._Cast_InterMountableComponentConnectionSystemDeflection(self)
