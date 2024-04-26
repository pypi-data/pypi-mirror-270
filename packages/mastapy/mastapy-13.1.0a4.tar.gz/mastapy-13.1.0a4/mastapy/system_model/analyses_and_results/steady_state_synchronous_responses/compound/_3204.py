"""InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3174,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3072,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3144,
        _3148,
        _3151,
        _3156,
        _3161,
        _3166,
        _3169,
        _3172,
        _3177,
        _3179,
        _3187,
        _3193,
        _3198,
        _3202,
        _3206,
        _3209,
        _3212,
        _3220,
        _3229,
        _3232,
        _3239,
        _3242,
        _3245,
        _3248,
        _3257,
        _3263,
        _3266,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
)


class InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
    _3174.ConnectionCompoundSteadyStateSynchronousResponse
):
    """InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _INTER_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
            parent: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3174.ConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3174.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3144,
            )

            return self._parent._cast(
                _3144.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3148.BeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3148,
            )

            return self._parent._cast(
                _3148.BeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3151,
            )

            return self._parent._cast(
                _3151.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.BevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3156,
            )

            return self._parent._cast(
                _3156.BevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def clutch_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3161.ClutchConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3161,
            )

            return self._parent._cast(
                _3161.ClutchConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3166.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3166,
            )

            return self._parent._cast(
                _3166.ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3169.ConceptGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3169,
            )

            return self._parent._cast(
                _3169.ConceptGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3172,
            )

            return self._parent._cast(
                _3172.ConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3177.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3177,
            )

            return self._parent._cast(
                _3177.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cvt_belt_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3179.CVTBeltConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3179,
            )

            return self._parent._cast(
                _3179.CVTBeltConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3187.CylindricalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3187,
            )

            return self._parent._cast(
                _3187.CylindricalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3193.FaceGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3193,
            )

            return self._parent._cast(
                _3193.FaceGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3198.GearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3198,
            )

            return self._parent._cast(
                _3198.GearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.HypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3206.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3206,
            )

            return self._parent._cast(
                _3206.KlingelnbergCycloPalloidConicalGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3209.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3209,
            )

            return self._parent._cast(
                _3209.KlingelnbergCycloPalloidHypoidGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3212,
            )

            return self._parent._cast(
                _3212.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_to_part_shear_coupling_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3220.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3220,
            )

            return self._parent._cast(
                _3220.PartToPartShearCouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def ring_pins_to_disc_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3229.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3229,
            )

            return self._parent._cast(
                _3229.RingPinsToDiscConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def rolling_ring_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3232.RollingRingConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3232,
            )

            return self._parent._cast(
                _3232.RollingRingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3239,
            )

            return self._parent._cast(
                _3239.SpiralBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def spring_damper_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3242.SpringDamperConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3242,
            )

            return self._parent._cast(
                _3242.SpringDamperConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3245,
            )

            return self._parent._cast(
                _3245.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3248,
            )

            return self._parent._cast(
                _3248.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def torque_converter_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3257.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3257,
            )

            return self._parent._cast(
                _3257.TorqueConverterConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3263.WormGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3263,
            )

            return self._parent._cast(
                _3263.WormGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3266,
            )

            return self._parent._cast(
                _3266.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.InterMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "List[_3072.InterMountableComponentConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.InterMountableComponentConnectionSteadyStateSynchronousResponse]

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
    ) -> "InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse(
            self
        )
