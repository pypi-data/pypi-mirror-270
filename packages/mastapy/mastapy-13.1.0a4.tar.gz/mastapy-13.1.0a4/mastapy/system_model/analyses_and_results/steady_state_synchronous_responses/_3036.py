"""ConceptGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3066,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ConceptGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import _6870
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3037,
        _3035,
        _3105,
        _3006,
        _3086,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ConceptGearSetSteadyStateSynchronousResponse")


class ConceptGearSetSteadyStateSynchronousResponse(
    _3066.GearSetSteadyStateSynchronousResponse
):
    """ConceptGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_ConceptGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
            parent: "ConceptGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_set_steady_state_synchronous_response(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_3066.GearSetSteadyStateSynchronousResponse":
            return self._parent._cast(_3066.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_3105.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3105,
            )

            return self._parent._cast(
                _3105.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_3006.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3006,
            )

            return self._parent._cast(
                _3006.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_3086.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3086,
            )

            return self._parent._cast(_3086.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_set_steady_state_synchronous_response(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
        ) -> "ConceptGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2540.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6870.ConceptGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3037.ConceptGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3037.ConceptGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3035.ConceptGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3035.ConceptGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearSetSteadyStateSynchronousResponse._Cast_ConceptGearSetSteadyStateSynchronousResponse":
        return self._Cast_ConceptGearSetSteadyStateSynchronousResponse(self)
