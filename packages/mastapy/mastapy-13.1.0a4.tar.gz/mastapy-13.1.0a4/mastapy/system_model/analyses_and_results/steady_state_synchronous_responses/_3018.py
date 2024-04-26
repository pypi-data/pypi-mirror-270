"""BevelDifferentialGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BevelDifferentialGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.static_loads import _6851
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3019,
        _3017,
        _3011,
        _3039,
        _3066,
        _3105,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetSteadyStateSynchronousResponse")


class BevelDifferentialGearSetSteadyStateSynchronousResponse(
    _3023.BevelGearSetSteadyStateSynchronousResponse
):
    """BevelDifferentialGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting BevelDifferentialGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
            parent: "BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3023.BevelGearSetSteadyStateSynchronousResponse":
            return self._parent._cast(_3023.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3011.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3011,
            )

            return self._parent._cast(
                _3011.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3039.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3039,
            )

            return self._parent._cast(
                _3039.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3066.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3066,
            )

            return self._parent._cast(_3066.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_steady_state_synchronous_response(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
        ) -> "BevelDifferentialGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BevelDifferentialGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6851.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3019.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3019.BevelDifferentialGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3017.BevelDifferentialGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3017.BevelDifferentialGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.BevelDifferentialGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetSteadyStateSynchronousResponse._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse":
        return self._Cast_BevelDifferentialGearSetSteadyStateSynchronousResponse(self)
