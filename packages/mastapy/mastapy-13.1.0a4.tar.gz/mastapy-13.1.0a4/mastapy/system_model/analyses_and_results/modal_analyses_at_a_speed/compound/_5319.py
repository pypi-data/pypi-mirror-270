"""CylindricalGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5330,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "CylindricalGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5189,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5317,
        _5318,
        _5354,
        _5368,
        _5270,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="CylindricalGearSetCompoundModalAnalysisAtASpeed")


class CylindricalGearSetCompoundModalAnalysisAtASpeed(
    _5330.GearSetCompoundModalAnalysisAtASpeed
):
    """CylindricalGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting CylindricalGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
            parent: "CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5330.GearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5330.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5270.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5354.PlanetaryGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5354,
            )

            return self._parent._cast(
                _5354.PlanetaryGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_speed(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
        ) -> "CylindricalGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "CylindricalGearSetCompoundModalAnalysisAtASpeed.TYPE",
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
    ) -> "List[_5189.CylindricalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearSetModalAnalysisAtASpeed]

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
    def cylindrical_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5317.CylindricalGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.CylindricalGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5318.CylindricalGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.CylindricalGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5189.CylindricalGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.CylindricalGearSetModalAnalysisAtASpeed]

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
    ) -> "CylindricalGearSetCompoundModalAnalysisAtASpeed._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_CylindricalGearSetCompoundModalAnalysisAtASpeed(self)
