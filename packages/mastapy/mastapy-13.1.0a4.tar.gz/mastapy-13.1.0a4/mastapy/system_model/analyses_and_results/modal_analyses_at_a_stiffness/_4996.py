"""SynchroniserModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4980,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "SynchroniserModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2625
    from mastapy.system_model.analyses_and_results.static_loads import _6995
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4880,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="SynchroniserModalAnalysisAtAStiffness")


class SynchroniserModalAnalysisAtAStiffness(
    _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """SynchroniserModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserModalAnalysisAtAStiffness"
    )

    class _Cast_SynchroniserModalAnalysisAtAStiffness:
        """Special nested class for casting SynchroniserModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
            parent: "SynchroniserModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_4980.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4980.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_4880.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4880,
            )

            return self._parent._cast(_4880.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_modal_analysis_at_a_stiffness(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
        ) -> "SynchroniserModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "SynchroniserModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2625.Synchroniser":
        """mastapy.system_model.part_model.couplings.Synchroniser

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6995.SynchroniserLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserModalAnalysisAtAStiffness._Cast_SynchroniserModalAnalysisAtAStiffness":
        return self._Cast_SynchroniserModalAnalysisAtAStiffness(self)
