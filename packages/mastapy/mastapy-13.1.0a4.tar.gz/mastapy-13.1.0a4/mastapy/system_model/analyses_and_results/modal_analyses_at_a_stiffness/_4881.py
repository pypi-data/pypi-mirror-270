"""AbstractShaftModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4882,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4925,
        _4978,
        _4905,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysisAtAStiffness")


class AbstractShaftModalAnalysisAtAStiffness(
    _4882.AbstractShaftOrHousingModalAnalysisAtAStiffness
):
    """AbstractShaftModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
            parent: "AbstractShaftModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4882.AbstractShaftOrHousingModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4882.AbstractShaftOrHousingModalAnalysisAtAStiffness
            )

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4905,
            )

            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4925.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(_4925.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "_4978.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(_4978.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
        ) -> "AbstractShaftModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "AbstractShaftModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftModalAnalysisAtAStiffness._Cast_AbstractShaftModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftModalAnalysisAtAStiffness(self)
