"""ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3415,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2349
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3395,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3403,
        _3431,
        _3457,
        _3463,
        _3433,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft"
)


class ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
    _3415.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3415.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3415.BevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3403.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3403,
            )

            return self._parent._cast(
                _3403.AGMAGleasonConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3431.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3431,
            )

            return self._parent._cast(
                _3431.ConicalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3457.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3457,
            )

            return self._parent._cast(
                _3457.GearMeshCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3463.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3463,
            )

            return self._parent._cast(
                _3463.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3433,
            )

            return self._parent._cast(
                _3433.ConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2349.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3395.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3395.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
