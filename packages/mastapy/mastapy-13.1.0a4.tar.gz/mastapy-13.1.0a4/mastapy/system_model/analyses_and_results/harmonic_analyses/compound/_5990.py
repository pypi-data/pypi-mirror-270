"""PlanetCarrierCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5982
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "PlanetCarrierCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2487
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5821
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="PlanetCarrierCompoundHarmonicAnalysis")


class PlanetCarrierCompoundHarmonicAnalysis(
    _5982.MountableComponentCompoundHarmonicAnalysis
):
    """PlanetCarrierCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierCompoundHarmonicAnalysis"
    )

    class _Cast_PlanetCarrierCompoundHarmonicAnalysis:
        """Special nested class for casting PlanetCarrierCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
            parent: "PlanetCarrierCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planet_carrier_compound_harmonic_analysis(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
        ) -> "PlanetCarrierCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetCarrierCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2487.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5821.PlanetCarrierHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5821.PlanetCarrierHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.PlanetCarrierHarmonicAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "PlanetCarrierCompoundHarmonicAnalysis._Cast_PlanetCarrierCompoundHarmonicAnalysis":
        return self._Cast_PlanetCarrierCompoundHarmonicAnalysis(self)
