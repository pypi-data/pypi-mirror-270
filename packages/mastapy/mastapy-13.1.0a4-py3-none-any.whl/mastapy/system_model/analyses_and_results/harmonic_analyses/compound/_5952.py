"""CylindricalGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5963
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CylindricalGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2543
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5753
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5955,
        _5982,
        _5930,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearCompoundHarmonicAnalysis")


class CylindricalGearCompoundHarmonicAnalysis(_5963.GearCompoundHarmonicAnalysis):
    """CylindricalGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundHarmonicAnalysis"
    )

    class _Cast_CylindricalGearCompoundHarmonicAnalysis:
        """Special nested class for casting CylindricalGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
            parent: "CylindricalGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_5963.GearCompoundHarmonicAnalysis":
            return self._parent._cast(_5963.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_5982.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_5930.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5930,
            )

            return self._parent._cast(_5930.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "_5955.CylindricalPlanetGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5955,
            )

            return self._parent._cast(
                _5955.CylindricalPlanetGearCompoundHarmonicAnalysis
            )

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
        ) -> "CylindricalGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2543.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

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
    ) -> "List[_5753.CylindricalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis]

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
    def planetaries(self: Self) -> "List[CylindricalGearCompoundHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.compound.CylindricalGearCompoundHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5753.CylindricalGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalGearHarmonicAnalysis]

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
    ) -> "CylindricalGearCompoundHarmonicAnalysis._Cast_CylindricalGearCompoundHarmonicAnalysis":
        return self._Cast_CylindricalGearCompoundHarmonicAnalysis(self)
