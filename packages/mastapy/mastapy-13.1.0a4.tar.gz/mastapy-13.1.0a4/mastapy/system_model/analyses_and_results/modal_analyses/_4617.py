"""ClutchHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4634
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ClutchHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2597
    from mastapy.system_model.analyses_and_results.static_loads import _6860
    from mastapy.system_model.analyses_and_results.system_deflections import _2735
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4681,
        _4620,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ClutchHalfModalAnalysis",)


Self = TypeVar("Self", bound="ClutchHalfModalAnalysis")


class ClutchHalfModalAnalysis(_4634.CouplingHalfModalAnalysis):
    """ClutchHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ClutchHalfModalAnalysis")

    class _Cast_ClutchHalfModalAnalysis:
        """Special nested class for casting ClutchHalfModalAnalysis to subclasses."""

        def __init__(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
            parent: "ClutchHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4634.CouplingHalfModalAnalysis":
            return self._parent._cast(_4634.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4681.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis",
        ) -> "ClutchHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ClutchHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2597.ClutchHalf":
        """mastapy.system_model.part_model.couplings.ClutchHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6860.ClutchHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ClutchHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2735.ClutchHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ClutchHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ClutchHalfModalAnalysis._Cast_ClutchHalfModalAnalysis":
        return self._Cast_ClutchHalfModalAnalysis(self)
