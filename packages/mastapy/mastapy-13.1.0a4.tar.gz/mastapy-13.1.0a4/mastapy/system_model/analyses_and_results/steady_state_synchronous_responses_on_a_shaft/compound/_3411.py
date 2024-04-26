"""BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3416,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3280,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3409,
        _3410,
        _3404,
        _3432,
        _3458,
        _3496,
        _3398,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self",
    bound="BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)


class BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3416.BevelGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3404,
            )

            return self._parent._cast(
                _3404.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3432,
            )

            return self._parent._cast(
                _3432.ConicalGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3458,
            )

            return self._parent._cast(
                _3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3409.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BevelDifferentialGearCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.BevelDifferentialGearsCompoundSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3410.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.BevelDifferentialGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.BevelDifferentialMeshesCompoundSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3280.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.BevelDifferentialGearSetSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_BevelDifferentialGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
