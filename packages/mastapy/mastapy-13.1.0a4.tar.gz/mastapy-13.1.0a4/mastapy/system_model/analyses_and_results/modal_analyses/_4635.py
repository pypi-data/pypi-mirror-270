"""CouplingModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "CouplingModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4618,
        _4623,
        _4688,
        _4711,
        _4725,
        _4595,
        _4685,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingModalAnalysis",)


Self = TypeVar("Self", bound="CouplingModalAnalysis")


class CouplingModalAnalysis(_4705.SpecialisedAssemblyModalAnalysis):
    """CouplingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingModalAnalysis")

    class _Cast_CouplingModalAnalysis:
        """Special nested class for casting CouplingModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
            parent: "CouplingModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4705.SpecialisedAssemblyModalAnalysis":
            return self._parent._cast(_4705.SpecialisedAssemblyModalAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4595.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4595

            return self._parent._cast(_4595.AbstractAssemblyModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4685.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4685

            return self._parent._cast(_4685.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4618.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.ClutchModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4623.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.ConceptCouplingModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4688.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4688

            return self._parent._cast(_4688.PartToPartShearCouplingModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4711.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4711

            return self._parent._cast(_4711.SpringDamperModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "_4725.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4725

            return self._parent._cast(_4725.TorqueConverterModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis",
        ) -> "CouplingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingModalAnalysis._Cast_CouplingModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2602.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2754.CouplingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingModalAnalysis._Cast_CouplingModalAnalysis":
        return self._Cast_CouplingModalAnalysis(self)
