"""CouplingHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5836
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2602
    from mastapy.system_model.analyses_and_results.system_deflections import _2754
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5728,
        _5734,
        _5817,
        _5843,
        _5858,
        _5704,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHarmonicAnalysis")


class CouplingHarmonicAnalysis(_5836.SpecialisedAssemblyHarmonicAnalysis):
    """CouplingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHarmonicAnalysis")

    class _Cast_CouplingHarmonicAnalysis:
        """Special nested class for casting CouplingHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
            parent: "CouplingHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5836.SpecialisedAssemblyHarmonicAnalysis":
            return self._parent._cast(_5836.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5704.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.AbstractAssemblyHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5728.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5728,
            )

            return self._parent._cast(_5728.ClutchHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5734.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5734,
            )

            return self._parent._cast(_5734.ConceptCouplingHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5817.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5817,
            )

            return self._parent._cast(_5817.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5843.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.SpringDamperHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "_5858.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5858,
            )

            return self._parent._cast(_5858.TorqueConverterHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis",
        ) -> "CouplingHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHarmonicAnalysis.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "CouplingHarmonicAnalysis._Cast_CouplingHarmonicAnalysis":
        return self._Cast_CouplingHarmonicAnalysis(self)
