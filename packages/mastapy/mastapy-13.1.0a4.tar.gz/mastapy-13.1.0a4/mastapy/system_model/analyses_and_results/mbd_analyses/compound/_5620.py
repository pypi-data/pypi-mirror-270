"""InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5473
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5560,
        _5564,
        _5567,
        _5572,
        _5577,
        _5582,
        _5585,
        _5588,
        _5593,
        _5595,
        _5603,
        _5609,
        _5614,
        _5618,
        _5622,
        _5625,
        _5628,
        _5636,
        _5645,
        _5648,
        _5655,
        _5658,
        _5661,
        _5664,
        _5673,
        _5679,
        _5682,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
)


class InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5590.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5590.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.AGMAGleasonConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5564.BeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5564,
            )

            return self._parent._cast(
                _5564.BeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(
                _5567.BevelDifferentialGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5572.BevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5572,
            )

            return self._parent._cast(
                _5572.BevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def clutch_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5577.ClutchConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5577,
            )

            return self._parent._cast(
                _5577.ClutchConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5582.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5582,
            )

            return self._parent._cast(
                _5582.ConceptCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5585.ConceptGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5585,
            )

            return self._parent._cast(
                _5585.ConceptGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5588.ConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5588,
            )

            return self._parent._cast(
                _5588.ConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5593.CouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(
                _5593.CouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_belt_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5595.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5595,
            )

            return self._parent._cast(
                _5595.CVTBeltConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5603.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.CylindricalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5609.FaceGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(
                _5609.FaceGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5614.GearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5614,
            )

            return self._parent._cast(_5614.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5618.HypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(
                _5618.HypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5622.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5622,
            )

            return self._parent._cast(
                _5622.KlingelnbergCycloPalloidConicalGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5625.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5625,
            )

            return self._parent._cast(
                _5625.KlingelnbergCycloPalloidHypoidGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5628.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.PartToPartShearCouplingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5645.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.RingPinsToDiscConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5648.RollingRingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5648,
            )

            return self._parent._cast(
                _5648.RollingRingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5655.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5655,
            )

            return self._parent._cast(
                _5655.SpiralBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5658.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5658,
            )

            return self._parent._cast(
                _5658.SpringDamperConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5661.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5661,
            )

            return self._parent._cast(
                _5661.StraightBevelDiffGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5664.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5664,
            )

            return self._parent._cast(
                _5664.StraightBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5673.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5673,
            )

            return self._parent._cast(
                _5673.TorqueConverterConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5679.WormGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5679,
            )

            return self._parent._cast(
                _5679.WormGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5682.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5682,
            )

            return self._parent._cast(
                _5682.ZerolBevelGearMeshCompoundMultibodyDynamicsAnalysis
            )

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5473.InterMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.InterMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
