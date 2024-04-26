"""CouplingDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6325,
        _6330,
        _6386,
        _6408,
        _6423,
        _6303,
        _6384,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingDynamicAnalysis")


class CouplingDynamicAnalysis(_6403.SpecialisedAssemblyDynamicAnalysis):
    """CouplingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingDynamicAnalysis")

    class _Cast_CouplingDynamicAnalysis:
        """Special nested class for casting CouplingDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
            parent: "CouplingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6403.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6403.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6303.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6303

            return self._parent._cast(_6303.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6384.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6325.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6325

            return self._parent._cast(_6325.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6330.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.ConceptCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6386.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.PartToPartShearCouplingDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6408.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.SpringDamperDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6423.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6423

            return self._parent._cast(_6423.TorqueConverterDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "CouplingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingDynamicAnalysis.TYPE"):
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
    def cast_to(self: Self) -> "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis":
        return self._Cast_CouplingDynamicAnalysis(self)
