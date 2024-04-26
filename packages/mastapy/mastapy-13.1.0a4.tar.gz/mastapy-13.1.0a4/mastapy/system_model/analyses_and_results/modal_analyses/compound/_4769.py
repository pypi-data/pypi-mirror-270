"""BevelGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4757
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BevelGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4613
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4764,
        _4852,
        _4858,
        _4861,
        _4879,
        _4785,
        _4811,
        _4849,
        _4751,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BevelGearSetCompoundModalAnalysis")


class BevelGearSetCompoundModalAnalysis(
    _4757.AGMAGleasonConicalGearSetCompoundModalAnalysis
):
    """BevelGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetCompoundModalAnalysis")

    class _Cast_BevelGearSetCompoundModalAnalysis:
        """Special nested class for casting BevelGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
            parent: "BevelGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4757.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            return self._parent._cast(
                _4757.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4785.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4811.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4849.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4751.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4764.BevelDifferentialGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4764,
            )

            return self._parent._cast(
                _4764.BevelDifferentialGearSetCompoundModalAnalysis
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4852.SpiralBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.SpiralBevelGearSetCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4858.StraightBevelDiffGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4858,
            )

            return self._parent._cast(
                _4858.StraightBevelDiffGearSetCompoundModalAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4861.StraightBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4861,
            )

            return self._parent._cast(_4861.StraightBevelGearSetCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "_4879.ZerolBevelGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4879,
            )

            return self._parent._cast(_4879.ZerolBevelGearSetCompoundModalAnalysis)

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
        ) -> "BevelGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearSetCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4613.BevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis]

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
    ) -> "List[_4613.BevelGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BevelGearSetModalAnalysis]

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
    ) -> "BevelGearSetCompoundModalAnalysis._Cast_BevelGearSetCompoundModalAnalysis":
        return self._Cast_BevelGearSetCompoundModalAnalysis(self)
