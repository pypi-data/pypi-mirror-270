"""CycloidalAssemblyModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CycloidalAssemblyModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2586
    from mastapy.system_model.analyses_and_results.static_loads import _6884
    from mastapy.system_model.analyses_and_results.system_deflections import _2758
    from mastapy.system_model.analyses_and_results.modal_analyses import _4595, _4685
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalAssemblyModalAnalysis",)


Self = TypeVar("Self", bound="CycloidalAssemblyModalAnalysis")


class CycloidalAssemblyModalAnalysis(_4705.SpecialisedAssemblyModalAnalysis):
    """CycloidalAssemblyModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CycloidalAssemblyModalAnalysis")

    class _Cast_CycloidalAssemblyModalAnalysis:
        """Special nested class for casting CycloidalAssemblyModalAnalysis to subclasses."""

        def __init__(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
            parent: "CycloidalAssemblyModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
        ) -> "CycloidalAssemblyModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CycloidalAssemblyModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2586.CycloidalAssembly":
        """mastapy.system_model.part_model.cycloidal.CycloidalAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6884.CycloidalAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2758.CycloidalAssemblySystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CycloidalAssemblySystemDeflection

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
    ) -> "CycloidalAssemblyModalAnalysis._Cast_CycloidalAssemblyModalAnalysis":
        return self._Cast_CycloidalAssemblyModalAnalysis(self)
