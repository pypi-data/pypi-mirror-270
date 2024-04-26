"""CouplingHalfCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CouplingHalfCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5744
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5928,
        _5933,
        _5947,
        _5987,
        _5993,
        _5997,
        _6009,
        _6019,
        _6020,
        _6021,
        _6024,
        _6025,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfCompoundHarmonicAnalysis")


class CouplingHalfCompoundHarmonicAnalysis(
    _5982.MountableComponentCompoundHarmonicAnalysis
):
    """CouplingHalfCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfCompoundHarmonicAnalysis")

    class _Cast_CouplingHalfCompoundHarmonicAnalysis:
        """Special nested class for casting CouplingHalfCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
            parent: "CouplingHalfCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5928.ClutchHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5928,
            )

            return self._parent._cast(_5928.ClutchHalfCompoundHarmonicAnalysis)

        @property
        def concept_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5933.ConceptCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5933,
            )

            return self._parent._cast(_5933.ConceptCouplingHalfCompoundHarmonicAnalysis)

        @property
        def cvt_pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5947.CVTPulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5947,
            )

            return self._parent._cast(_5947.CVTPulleyCompoundHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5987.PartToPartShearCouplingHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5987,
            )

            return self._parent._cast(
                _5987.PartToPartShearCouplingHalfCompoundHarmonicAnalysis
            )

        @property
        def pulley_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5993.PulleyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5993,
            )

            return self._parent._cast(_5993.PulleyCompoundHarmonicAnalysis)

        @property
        def rolling_ring_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_5997.RollingRingCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5997,
            )

            return self._parent._cast(_5997.RollingRingCompoundHarmonicAnalysis)

        @property
        def spring_damper_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6009.SpringDamperHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(_6009.SpringDamperHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6019.SynchroniserHalfCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6019,
            )

            return self._parent._cast(_6019.SynchroniserHalfCompoundHarmonicAnalysis)

        @property
        def synchroniser_part_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6020.SynchroniserPartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6020,
            )

            return self._parent._cast(_6020.SynchroniserPartCompoundHarmonicAnalysis)

        @property
        def synchroniser_sleeve_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6021.SynchroniserSleeveCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6021,
            )

            return self._parent._cast(_6021.SynchroniserSleeveCompoundHarmonicAnalysis)

        @property
        def torque_converter_pump_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6024.TorqueConverterPumpCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6024,
            )

            return self._parent._cast(_6024.TorqueConverterPumpCompoundHarmonicAnalysis)

        @property
        def torque_converter_turbine_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "_6025.TorqueConverterTurbineCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6025,
            )

            return self._parent._cast(
                _6025.TorqueConverterTurbineCompoundHarmonicAnalysis
            )

        @property
        def coupling_half_compound_harmonic_analysis(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
        ) -> "CouplingHalfCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CouplingHalfCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5744.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5744.CouplingHalfHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CouplingHalfHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfCompoundHarmonicAnalysis._Cast_CouplingHalfCompoundHarmonicAnalysis":
        return self._Cast_CouplingHalfCompoundHarmonicAnalysis(self)
