"""StraightBevelDiffGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "StraightBevelDiffGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2564
    from mastapy.system_model.analyses_and_results.modal_analyses import _4714
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4856,
        _4857,
        _4757,
        _4785,
        _4811,
        _4849,
        _4751,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearSetCompoundModalAnalysis")


class StraightBevelDiffGearSetCompoundModalAnalysis(
    _4769.BevelGearSetCompoundModalAnalysis
):
    """StraightBevelDiffGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearSetCompoundModalAnalysis"
    )

    class _Cast_StraightBevelDiffGearSetCompoundModalAnalysis:
        """Special nested class for casting StraightBevelDiffGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
            parent: "StraightBevelDiffGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4769.BevelGearSetCompoundModalAnalysis":
            return self._parent._cast(_4769.BevelGearSetCompoundModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4757.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4757,
            )

            return self._parent._cast(
                _4757.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4785.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4811.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4849.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4751.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
        ) -> "StraightBevelDiffGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis",
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
        instance_to_wrap: "StraightBevelDiffGearSetCompoundModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2564.StraightBevelDiffGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGearSet

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
    ) -> "List[_4714.StraightBevelDiffGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis]

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
    def straight_bevel_diff_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4856.StraightBevelDiffGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_diff_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4857.StraightBevelDiffGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.StraightBevelDiffGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4714.StraightBevelDiffGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.StraightBevelDiffGearSetModalAnalysis]

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
    ) -> "StraightBevelDiffGearSetCompoundModalAnalysis._Cast_StraightBevelDiffGearSetCompoundModalAnalysis":
        return self._Cast_StraightBevelDiffGearSetCompoundModalAnalysis(self)
