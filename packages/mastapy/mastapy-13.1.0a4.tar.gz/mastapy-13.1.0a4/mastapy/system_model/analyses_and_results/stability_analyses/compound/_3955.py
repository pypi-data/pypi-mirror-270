"""ConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "ConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3821
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3923,
        _3925,
        _3929,
        _3932,
        _3937,
        _3942,
        _3944,
        _3947,
        _3950,
        _3953,
        _3958,
        _3960,
        _3964,
        _3966,
        _3968,
        _3974,
        _3979,
        _3983,
        _3985,
        _3987,
        _3990,
        _3993,
        _4001,
        _4003,
        _4010,
        _4013,
        _4017,
        _4020,
        _4023,
        _4026,
        _4029,
        _4038,
        _4044,
        _4047,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundStabilityAnalysis")


class ConnectionCompoundStabilityAnalysis(_7565.ConnectionCompoundAnalysis):
    """ConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundStabilityAnalysis")

    class _Cast_ConnectionCompoundStabilityAnalysis:
        """Special nested class for casting ConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
            parent: "ConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3923.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3923,
            )

            return self._parent._cast(
                _3923.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3925.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3925,
            )

            return self._parent._cast(
                _3925.AGMAGleasonConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3929.BeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3929,
            )

            return self._parent._cast(_3929.BeltConnectionCompoundStabilityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3932.BevelDifferentialGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3932,
            )

            return self._parent._cast(
                _3932.BevelDifferentialGearMeshCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3937.BevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3937,
            )

            return self._parent._cast(_3937.BevelGearMeshCompoundStabilityAnalysis)

        @property
        def clutch_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3942.ClutchConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3942,
            )

            return self._parent._cast(_3942.ClutchConnectionCompoundStabilityAnalysis)

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3944.CoaxialConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3944,
            )

            return self._parent._cast(_3944.CoaxialConnectionCompoundStabilityAnalysis)

        @property
        def concept_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3947.ConceptCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3947,
            )

            return self._parent._cast(
                _3947.ConceptCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def concept_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3950.ConceptGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3950,
            )

            return self._parent._cast(_3950.ConceptGearMeshCompoundStabilityAnalysis)

        @property
        def conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3953.ConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3953,
            )

            return self._parent._cast(_3953.ConicalGearMeshCompoundStabilityAnalysis)

        @property
        def coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3958.CouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3958,
            )

            return self._parent._cast(_3958.CouplingConnectionCompoundStabilityAnalysis)

        @property
        def cvt_belt_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3960.CVTBeltConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3960,
            )

            return self._parent._cast(_3960.CVTBeltConnectionCompoundStabilityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3964.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3964,
            )

            return self._parent._cast(
                _3964.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3966.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3966,
            )

            return self._parent._cast(
                _3966.CycloidalDiscPlanetaryBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3968.CylindricalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3968,
            )

            return self._parent._cast(
                _3968.CylindricalGearMeshCompoundStabilityAnalysis
            )

        @property
        def face_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3974.FaceGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3974,
            )

            return self._parent._cast(_3974.FaceGearMeshCompoundStabilityAnalysis)

        @property
        def gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3979.GearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3979,
            )

            return self._parent._cast(_3979.GearMeshCompoundStabilityAnalysis)

        @property
        def hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3983.HypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3983,
            )

            return self._parent._cast(_3983.HypoidGearMeshCompoundStabilityAnalysis)

        @property
        def inter_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3985.InterMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3985,
            )

            return self._parent._cast(
                _3985.InterMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3987.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3987,
            )

            return self._parent._cast(
                _3987.KlingelnbergCycloPalloidConicalGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_3990.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3990,
            )

            return self._parent._cast(
                _3990.KlingelnbergCycloPalloidHypoidGearMeshCompoundStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3993.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3993,
            )

            return self._parent._cast(
                _3993.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4001.PartToPartShearCouplingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4001,
            )

            return self._parent._cast(
                _4001.PartToPartShearCouplingConnectionCompoundStabilityAnalysis
            )

        @property
        def planetary_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4003.PlanetaryConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4003,
            )

            return self._parent._cast(
                _4003.PlanetaryConnectionCompoundStabilityAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4010.RingPinsToDiscConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4010,
            )

            return self._parent._cast(
                _4010.RingPinsToDiscConnectionCompoundStabilityAnalysis
            )

        @property
        def rolling_ring_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4013.RollingRingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(
                _4013.RollingRingConnectionCompoundStabilityAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4017.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4017,
            )

            return self._parent._cast(
                _4017.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4020.SpiralBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4020,
            )

            return self._parent._cast(
                _4020.SpiralBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def spring_damper_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4023.SpringDamperConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4023,
            )

            return self._parent._cast(
                _4023.SpringDamperConnectionCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4026.StraightBevelDiffGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4026,
            )

            return self._parent._cast(
                _4026.StraightBevelDiffGearMeshCompoundStabilityAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4029.StraightBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4029,
            )

            return self._parent._cast(
                _4029.StraightBevelGearMeshCompoundStabilityAnalysis
            )

        @property
        def torque_converter_connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4038.TorqueConverterConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4038,
            )

            return self._parent._cast(
                _4038.TorqueConverterConnectionCompoundStabilityAnalysis
            )

        @property
        def worm_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4044.WormGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4044,
            )

            return self._parent._cast(_4044.WormGearMeshCompoundStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "_4047.ZerolBevelGearMeshCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4047,
            )

            return self._parent._cast(_4047.ZerolBevelGearMeshCompoundStabilityAnalysis)

        @property
        def connection_compound_stability_analysis(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
        ) -> "ConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3821.ConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectionStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3821.ConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.ConnectionStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "ConnectionCompoundStabilityAnalysis._Cast_ConnectionCompoundStabilityAnalysis"
    ):
        return self._Cast_ConnectionCompoundStabilityAnalysis(self)
