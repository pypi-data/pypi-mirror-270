"""AbstractShaftModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.system_deflections import _2710
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4641,
        _4702,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftModalAnalysis")


class AbstractShaftModalAnalysis(_4597.AbstractShaftOrHousingModalAnalysis):
    """AbstractShaftModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftModalAnalysis")

    class _Cast_AbstractShaftModalAnalysis:
        """Special nested class for casting AbstractShaftModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            parent: "AbstractShaftModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4597.AbstractShaftOrHousingModalAnalysis":
            return self._parent._cast(_4597.AbstractShaftOrHousingModalAnalysis)

        @property
        def component_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4641.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4641

            return self._parent._cast(_4641.CycloidalDiscModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "_4702.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.ShaftModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
        ) -> "AbstractShaftModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaftModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2710.AbstractShaftSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftModalAnalysis._Cast_AbstractShaftModalAnalysis":
        return self._Cast_AbstractShaftModalAnalysis(self)
