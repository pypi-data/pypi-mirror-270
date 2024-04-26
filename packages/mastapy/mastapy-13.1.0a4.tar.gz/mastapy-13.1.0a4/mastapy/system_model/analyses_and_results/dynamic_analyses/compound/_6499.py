"""InterMountableComponentConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6469
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "InterMountableComponentConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6439,
        _6443,
        _6446,
        _6451,
        _6456,
        _6461,
        _6464,
        _6467,
        _6472,
        _6474,
        _6482,
        _6488,
        _6493,
        _6497,
        _6501,
        _6504,
        _6507,
        _6515,
        _6524,
        _6527,
        _6534,
        _6537,
        _6540,
        _6543,
        _6552,
        _6558,
        _6561,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionCompoundDynamicAnalysis")


class InterMountableComponentConnectionCompoundDynamicAnalysis(
    _6469.ConnectionCompoundDynamicAnalysis
):
    """InterMountableComponentConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
    )

    class _Cast_InterMountableComponentConnectionCompoundDynamicAnalysis:
        """Special nested class for casting InterMountableComponentConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
            parent: "InterMountableComponentConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6439,
            )

            return self._parent._cast(
                _6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def belt_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6443.BeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6443,
            )

            return self._parent._cast(_6443.BeltConnectionCompoundDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6446.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(
                _6446.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6451.BevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6451,
            )

            return self._parent._cast(_6451.BevelGearMeshCompoundDynamicAnalysis)

        @property
        def clutch_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6456.ClutchConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6456,
            )

            return self._parent._cast(_6456.ClutchConnectionCompoundDynamicAnalysis)

        @property
        def concept_coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6461.ConceptCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6461,
            )

            return self._parent._cast(
                _6461.ConceptCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def concept_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6464.ConceptGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6464,
            )

            return self._parent._cast(_6464.ConceptGearMeshCompoundDynamicAnalysis)

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6467.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6472.CouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.CouplingConnectionCompoundDynamicAnalysis)

        @property
        def cvt_belt_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6474.CVTBeltConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6474,
            )

            return self._parent._cast(_6474.CVTBeltConnectionCompoundDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6482.CylindricalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(_6482.CylindricalGearMeshCompoundDynamicAnalysis)

        @property
        def face_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6488.FaceGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6488,
            )

            return self._parent._cast(_6488.FaceGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6493.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.GearMeshCompoundDynamicAnalysis)

        @property
        def hypoid_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6497.HypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6497,
            )

            return self._parent._cast(_6497.HypoidGearMeshCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6501,
            )

            return self._parent._cast(
                _6501.KlingelnbergCycloPalloidConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6504,
            )

            return self._parent._cast(
                _6504.KlingelnbergCycloPalloidHypoidGearMeshCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6507,
            )

            return self._parent._cast(
                _6507.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6515.PartToPartShearCouplingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.PartToPartShearCouplingConnectionCompoundDynamicAnalysis
            )

        @property
        def ring_pins_to_disc_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6524.RingPinsToDiscConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6524,
            )

            return self._parent._cast(
                _6524.RingPinsToDiscConnectionCompoundDynamicAnalysis
            )

        @property
        def rolling_ring_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6527.RollingRingConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6527,
            )

            return self._parent._cast(
                _6527.RollingRingConnectionCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6534.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def spring_damper_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6537.SpringDamperConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6537,
            )

            return self._parent._cast(
                _6537.SpringDamperConnectionCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6543.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(
                _6543.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def torque_converter_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6552.TorqueConverterConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6552,
            )

            return self._parent._cast(
                _6552.TorqueConverterConnectionCompoundDynamicAnalysis
            )

        @property
        def worm_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6558.WormGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6558,
            )

            return self._parent._cast(_6558.WormGearMeshCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "_6561.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6561,
            )

            return self._parent._cast(_6561.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
        ) -> "InterMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundDynamicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6370.InterMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis]

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
    ) -> "List[_6370.InterMountableComponentConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.InterMountableComponentConnectionDynamicAnalysis]

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
    ) -> "InterMountableComponentConnectionCompoundDynamicAnalysis._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis":
        return self._Cast_InterMountableComponentConnectionCompoundDynamicAnalysis(self)
