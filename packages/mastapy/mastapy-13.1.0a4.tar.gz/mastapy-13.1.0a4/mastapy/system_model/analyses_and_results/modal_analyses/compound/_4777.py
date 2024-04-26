"""ConceptCouplingCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4788
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "ConceptCouplingCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.modal_analyses import _4623
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4849,
        _4751,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingCompoundModalAnalysis",)


Self = TypeVar("Self", bound="ConceptCouplingCompoundModalAnalysis")


class ConceptCouplingCompoundModalAnalysis(_4788.CouplingCompoundModalAnalysis):
    """ConceptCouplingCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingCompoundModalAnalysis")

    class _Cast_ConceptCouplingCompoundModalAnalysis:
        """Special nested class for casting ConceptCouplingCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
            parent: "ConceptCouplingCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_modal_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_4788.CouplingCompoundModalAnalysis":
            return self._parent._cast(_4788.CouplingCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_4849.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_4751.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_coupling_compound_modal_analysis(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
        ) -> "ConceptCouplingCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "ConceptCouplingCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2599.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2599.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

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
    ) -> "List[_4623.ConceptCouplingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4623.ConceptCouplingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.ConceptCouplingModalAnalysis]

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
    ) -> "ConceptCouplingCompoundModalAnalysis._Cast_ConceptCouplingCompoundModalAnalysis":
        return self._Cast_ConceptCouplingCompoundModalAnalysis(self)
