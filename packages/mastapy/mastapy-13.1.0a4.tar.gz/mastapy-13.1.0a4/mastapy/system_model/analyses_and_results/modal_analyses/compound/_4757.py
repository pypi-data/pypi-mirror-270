"""AGMAGleasonConicalGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4785
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4601
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4764,
        _4769,
        _4815,
        _4852,
        _4858,
        _4861,
        _4879,
        _4811,
        _4849,
        _4751,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundModalAnalysis")


class AGMAGleasonConicalGearSetCompoundModalAnalysis(
    _4785.ConicalGearSetCompoundModalAnalysis
):
    """AGMAGleasonConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4785.ConicalGearSetCompoundModalAnalysis":
            return self._parent._cast(_4785.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4811.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4849.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4751.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4764.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(
                _4764.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4769.BevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.BevelGearSetCompoundModalAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4815.HypoidGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.HypoidGearSetCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4852.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4858.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(
                _4858.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4861.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "_4879.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4879,
            )

            return self._parent._cast(_4879.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4601.AGMAGleasonConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis]

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
    ) -> "List[_4601.AGMAGleasonConicalGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.AGMAGleasonConicalGearSetModalAnalysis]

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
    ) -> "AGMAGleasonConicalGearSetCompoundModalAnalysis._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundModalAnalysis(self)
