"""ConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7565
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6437,
        _6439,
        _6443,
        _6446,
        _6451,
        _6456,
        _6458,
        _6461,
        _6464,
        _6467,
        _6472,
        _6474,
        _6478,
        _6480,
        _6482,
        _6488,
        _6493,
        _6497,
        _6499,
        _6501,
        _6504,
        _6507,
        _6515,
        _6517,
        _6524,
        _6527,
        _6531,
        _6534,
        _6537,
        _6540,
        _6543,
        _6552,
        _6558,
        _6561,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConnectionCompoundDynamicAnalysis")


class ConnectionCompoundDynamicAnalysis(_7565.ConnectionCompoundAnalysis):
    """ConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionCompoundDynamicAnalysis")

    class _Cast_ConnectionCompoundDynamicAnalysis:
        """Special nested class for casting ConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
            parent: "ConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6437.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6437,
            )

            return self._parent._cast(
                _6437.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(
                _6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6443.BeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6446.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(
                _6446.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6451.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6456.ClutchConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def coaxial_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6458.CoaxialConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6458,
            )

            return self._parent._cast(_6458.CoaxialConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6461.ConceptCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(
                _6461.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConceptGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6467.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6472.CouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6474.CVTBeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6478.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6478,
            )

            return self._parent._cast(
                _6478.CycloidalDiscCentralBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6480.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6480,
            )

            return self._parent._cast(
                _6480.CycloidalDiscPlanetaryBearingConnectionCompoundDynamicAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6482.CylindricalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6488.FaceGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6493.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6497.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6499.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(
                _6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(
                _6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6515.PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6517.PlanetaryConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6517,
            )

            return self._parent._cast(_6517.PlanetaryConnectionCompoundDynamicAnalysis)

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6524.RingPinsToDiscConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(
                _6524.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6527.RollingRingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(
                _6527.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6531.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6531,
            )

            return self._parent._cast(
                _6531.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6534.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6537.SpringDamperConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6537,
            )

            return self._parent._cast(
                _6537.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6543.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(
                _6543.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6552.TorqueConverterConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6552,
            )

            return self._parent._cast(
                _6552.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6558.WormGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6558,
            )

            return self._parent._cast(_6558.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "_6561.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6561,
            )

            return self._parent._cast(_6561.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def connection_compound_dynamic_analysis(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
        ) -> "ConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConnectionCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6338.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

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
    ) -> "List[_6338.ConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConnectionDynamicAnalysis]

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
    ) -> "ConnectionCompoundDynamicAnalysis._Cast_ConnectionCompoundDynamicAnalysis":
        return self._Cast_ConnectionCompoundDynamicAnalysis(self)
