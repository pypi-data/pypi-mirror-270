"""ZerolBevelGearSetCompoundModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
    _5288,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound",
    "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2572
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5269,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
        _5396,
        _5397,
        _5276,
        _5304,
        _5330,
        _5368,
        _5270,
        _5349,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetCompoundModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="ZerolBevelGearSetCompoundModalAnalysisAtASpeed")


class ZerolBevelGearSetCompoundModalAnalysisAtASpeed(
    _5288.BevelGearSetCompoundModalAnalysisAtASpeed
):
    """ZerolBevelGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed"
    )

    class _Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed:
        """Special nested class for casting ZerolBevelGearSetCompoundModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
            parent: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5288.BevelGearSetCompoundModalAnalysisAtASpeed":
            return self._parent._cast(_5288.BevelGearSetCompoundModalAnalysisAtASpeed)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5276.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5276,
            )

            return self._parent._cast(
                _5276.AGMAGleasonConicalGearSetCompoundModalAnalysisAtASpeed
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5304.ConicalGearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5304,
            )

            return self._parent._cast(_5304.ConicalGearSetCompoundModalAnalysisAtASpeed)

        @property
        def gear_set_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5330.GearSetCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5330,
            )

            return self._parent._cast(_5330.GearSetCompoundModalAnalysisAtASpeed)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5368,
            )

            return self._parent._cast(
                _5368.SpecialisedAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5270.AbstractAssemblyCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5270,
            )

            return self._parent._cast(
                _5270.AbstractAssemblyCompoundModalAnalysisAtASpeed
            )

        @property
        def part_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_5349.PartCompoundModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import (
                _5349,
            )

            return self._parent._cast(_5349.PartCompoundModalAnalysisAtASpeed)

        @property
        def part_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_speed(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
        ) -> "ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed",
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
        instance_to_wrap: "ZerolBevelGearSetCompoundModalAnalysisAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2572.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5269.ZerolBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearSetModalAnalysisAtASpeed]

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
    def zerol_bevel_gears_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5396.ZerolBevelGearCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.ZerolBevelGearCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_compound_modal_analysis_at_a_speed(
        self: Self,
    ) -> "List[_5397.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound.ZerolBevelGearMeshCompoundModalAnalysisAtASpeed]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesCompoundModalAnalysisAtASpeed

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5269.ZerolBevelGearSetModalAnalysisAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.ZerolBevelGearSetModalAnalysisAtASpeed]

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
    ) -> "ZerolBevelGearSetCompoundModalAnalysisAtASpeed._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed":
        return self._Cast_ZerolBevelGearSetCompoundModalAnalysisAtASpeed(self)
