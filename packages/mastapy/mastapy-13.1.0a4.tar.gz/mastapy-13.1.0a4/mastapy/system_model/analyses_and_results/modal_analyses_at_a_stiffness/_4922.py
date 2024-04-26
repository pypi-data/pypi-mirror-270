"""CVTPulleyModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4970,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "CVTPulleyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4918,
        _4959,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="CVTPulleyModalAnalysisAtAStiffness")


class CVTPulleyModalAnalysisAtAStiffness(_4970.PulleyModalAnalysisAtAStiffness):
    """CVTPulleyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyModalAnalysisAtAStiffness")

    class _Cast_CVTPulleyModalAnalysisAtAStiffness:
        """Special nested class for casting CVTPulleyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
            parent: "CVTPulleyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def pulley_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_4970.PulleyModalAnalysisAtAStiffness":
            return self._parent._cast(_4970.PulleyModalAnalysisAtAStiffness)

        @property
        def coupling_half_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_4918.CouplingHalfModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4918,
            )

            return self._parent._cast(_4918.CouplingHalfModalAnalysisAtAStiffness)

        @property
        def mountable_component_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_4959.MountableComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4959,
            )

            return self._parent._cast(_4959.MountableComponentModalAnalysisAtAStiffness)

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_modal_analysis_at_a_stiffness(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
        ) -> "CVTPulleyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "CVTPulleyModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyModalAnalysisAtAStiffness._Cast_CVTPulleyModalAnalysisAtAStiffness":
        return self._Cast_CVTPulleyModalAnalysisAtAStiffness(self)
