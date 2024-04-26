"""BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3543,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2319
    from mastapy.system_model.analyses_and_results.static_loads import _6850
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3531,
        _3559,
        _3585,
        _3592,
        _3562,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed"
)


class BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3543.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3559,
            )

            return self._parent._cast(
                _3559.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(
                _3585.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3592,
            )

            return self._parent._cast(
                _3592.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3562.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3562,
            )

            return self._parent._cast(
                _3562.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2319.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6850.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed":
        return (
            self._Cast_BevelDifferentialGearMeshSteadyStateSynchronousResponseAtASpeed(
                self
            )
        )
