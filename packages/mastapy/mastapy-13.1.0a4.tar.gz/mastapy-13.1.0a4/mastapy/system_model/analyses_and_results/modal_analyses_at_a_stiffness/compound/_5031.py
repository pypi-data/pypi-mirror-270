"""BoltedJointCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
    _5109,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "BoltedJointCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4899,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _5011,
        _5090,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="BoltedJointCompoundModalAnalysisAtAStiffness")


class BoltedJointCompoundModalAnalysisAtAStiffness(
    _5109.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
):
    """BoltedJointCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_BoltedJointCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting BoltedJointCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
            parent: "BoltedJointCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            return self._parent._cast(
                _5109.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(
                _5011.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_5090.PartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5090,
            )

            return self._parent._cast(_5090.PartCompoundModalAnalysisAtAStiffness)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
        ) -> "BoltedJointCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness",
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
        instance_to_wrap: "BoltedJointCompoundModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2461.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2461.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

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
    ) -> "List[_4899.BoltedJointModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BoltedJointModalAnalysisAtAStiffness]

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
    ) -> "List[_4899.BoltedJointModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.BoltedJointModalAnalysisAtAStiffness]

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
    ) -> "BoltedJointCompoundModalAnalysisAtAStiffness._Cast_BoltedJointCompoundModalAnalysisAtAStiffness":
        return self._Cast_BoltedJointCompoundModalAnalysisAtAStiffness(self)
