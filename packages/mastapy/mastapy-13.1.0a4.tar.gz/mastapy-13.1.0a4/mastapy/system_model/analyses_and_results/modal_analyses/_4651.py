"""ExternalCADModelModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4620
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ExternalCADModelModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.static_loads import _6910
    from mastapy.system_model.analyses_and_results.system_deflections import _2775
    from mastapy.system_model.analyses_and_results.modal_analyses import _4685
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ExternalCADModelModalAnalysis",)


Self = TypeVar("Self", bound="ExternalCADModelModalAnalysis")


class ExternalCADModelModalAnalysis(_4620.ComponentModalAnalysis):
    """ExternalCADModelModalAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ExternalCADModelModalAnalysis")

    class _Cast_ExternalCADModelModalAnalysis:
        """Special nested class for casting ExternalCADModelModalAnalysis to subclasses."""

        def __init__(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
            parent: "ExternalCADModelModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_4620.ComponentModalAnalysis":
            return self._parent._cast(_4620.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
        ) -> "ExternalCADModelModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ExternalCADModelModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.ExternalCADModel":
        """mastapy.system_model.part_model.ExternalCADModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6910.ExternalCADModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ExternalCADModelLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2775.ExternalCADModelSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ExternalCADModelSystemDeflection

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
    ) -> "ExternalCADModelModalAnalysis._Cast_ExternalCADModelModalAnalysis":
        return self._Cast_ExternalCADModelModalAnalysis(self)
