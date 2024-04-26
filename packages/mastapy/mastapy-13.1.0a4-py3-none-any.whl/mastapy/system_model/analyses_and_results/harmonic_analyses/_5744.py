"""CouplingHalfHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5812
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "CouplingHalfHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.system_deflections import _2753
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5727,
        _5733,
        _5748,
        _5816,
        _5824,
        _5830,
        _5842,
        _5853,
        _5855,
        _5856,
        _5859,
        _5860,
        _5731,
        _5814,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfHarmonicAnalysis")


class CouplingHalfHarmonicAnalysis(_5812.MountableComponentHarmonicAnalysis):
    """CouplingHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfHarmonicAnalysis")

    class _Cast_CouplingHalfHarmonicAnalysis:
        """Special nested class for casting CouplingHalfHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            parent: "CouplingHalfHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5812.MountableComponentHarmonicAnalysis":
            return self._parent._cast(_5812.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5731.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5814.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5727.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.ClutchHalfHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5733.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5748.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.CVTPulleyHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5816.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5824.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.PulleyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5830.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.RollingRingHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5842.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.SpringDamperHalfHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5853.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5853,
            )

            return self._parent._cast(_5853.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5855.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5855,
            )

            return self._parent._cast(_5855.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5856.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5856,
            )

            return self._parent._cast(_5856.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5859.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5859,
            )

            return self._parent._cast(_5859.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "_5860.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5860,
            )

            return self._parent._cast(_5860.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
        ) -> "CouplingHalfHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2753.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

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
    ) -> "CouplingHalfHarmonicAnalysis._Cast_CouplingHalfHarmonicAnalysis":
        return self._Cast_CouplingHalfHarmonicAnalysis(self)
