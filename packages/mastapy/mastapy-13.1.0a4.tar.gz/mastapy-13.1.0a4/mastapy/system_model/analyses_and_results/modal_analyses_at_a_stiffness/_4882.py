"""AbstractShaftOrHousingModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4905,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "AbstractShaftOrHousingModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4881,
        _4925,
        _4937,
        _4978,
        _4961,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysisAtAStiffness")


class AbstractShaftOrHousingModalAnalysisAtAStiffness(
    _4905.ComponentModalAnalysisAtAStiffness
):
    """AbstractShaftOrHousingModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness"
    )

    class _Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
            parent: "AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def component_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4905.ComponentModalAnalysisAtAStiffness":
            return self._parent._cast(_4905.ComponentModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4961.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4961,
            )

            return self._parent._cast(_4961.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4881.AbstractShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4881,
            )

            return self._parent._cast(_4881.AbstractShaftModalAnalysisAtAStiffness)

        @property
        def cycloidal_disc_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4925.CycloidalDiscModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4925,
            )

            return self._parent._cast(_4925.CycloidalDiscModalAnalysisAtAStiffness)

        @property
        def fe_part_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4937.FEPartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4937,
            )

            return self._parent._cast(_4937.FEPartModalAnalysisAtAStiffness)

        @property
        def shaft_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "_4978.ShaftModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4978,
            )

            return self._parent._cast(_4978.ShaftModalAnalysisAtAStiffness)

        @property
        def abstract_shaft_or_housing_modal_analysis_at_a_stiffness(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
        ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness",
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
        instance_to_wrap: "AbstractShaftOrHousingModalAnalysisAtAStiffness.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2454.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingModalAnalysisAtAStiffness._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness":
        return self._Cast_AbstractShaftOrHousingModalAnalysisAtAStiffness(self)
