"""ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3285,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _7014
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3397,
        _3395,
        _3273,
        _3301,
        _3327,
        _3366,
        _3268,
        _3347,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft")


class ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft(
    _3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft
):
    """ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3285.BevelGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3273,
            )

            return self._parent._cast(
                _3273.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3301,
            )

            return self._parent._cast(
                _3301.ConicalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3327.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3327,
            )

            return self._parent._cast(
                _3327.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3366,
            )

            return self._parent._cast(
                _3366.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3268,
            )

            return self._parent._cast(
                _3268.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3347.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3347,
            )

            return self._parent._cast(_3347.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2572.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_7014.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3397.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_gears_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3397.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3395.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3395.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesSteadyStateSynchronousResponseOnAShaft

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ZerolBevelGearSetSteadyStateSynchronousResponseOnAShaft(self)
