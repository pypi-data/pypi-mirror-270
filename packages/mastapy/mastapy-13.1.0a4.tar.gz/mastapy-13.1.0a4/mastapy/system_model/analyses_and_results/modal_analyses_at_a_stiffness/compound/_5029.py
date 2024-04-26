"""BevelGearSetCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BevelGearSetCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4898,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5024,
        _5112,
        _5118,
        _5121,
        _5139,
        _5045,
        _5071,
        _5109,
        _5011,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BevelGearSetCompoundModalAnalysisAtAStiffness")


class BevelGearSetCompoundModalAnalysisAtAStiffness(
    _5017.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
):
    """BevelGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearSetCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_BevelGearSetCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BevelGearSetCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
            parent: "BevelGearSetCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5017.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5017.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5045.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5071.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5071,
            )

            return self._parent._cast(_5071.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5118.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5121.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5121,
            )

            return self._parent._cast(
                _5121.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "_5139.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5139,
            )

            return self._parent._cast(
                _5139.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
        ) -> "BevelGearSetCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BevelGearSetCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4898.BevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearSetModalAnalysisAtAStiffness]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4898.BevelGearSetModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BevelGearSetModalAnalysisAtAStiffness]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearSetCompoundModalAnalysisAtAStiffness._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness":
        return self._Cast_BevelGearSetCompoundModalAnalysisAtAStiffness(self)
