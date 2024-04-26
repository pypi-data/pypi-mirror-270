"""CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3458,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3316,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3445,
        _3446,
        _3482,
        _3496,
        _3398,
        _3477,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft"
)


class CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
    _3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
):
    """CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3458.GearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3496,
            )

            return self._parent._cast(
                _3496.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3398,
            )

            return self._parent._cast(
                _3398.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3477.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3477,
            )

            return self._parent._cast(
                _3477.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3482,
            )

            return self._parent._cast(
                _3482.PlanetaryGearSetCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response_on_a_shaft(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2544.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2544.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

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
    ) -> "List[_3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]

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
    def cylindrical_gears_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> "List[_3445.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CylindricalGearCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CylindricalGearsCompoundSteadyStateSynchronousResponseOnAShaft
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_steady_state_synchronous_response_on_a_shaft(
        self: Self,
    ) -> (
        "List[_3446.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound.CylindricalGearMeshCompoundSteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.CylindricalMeshesCompoundSteadyStateSynchronousResponseOnAShaft
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
    ) -> "List[_3316.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_CylindricalGearSetCompoundSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
