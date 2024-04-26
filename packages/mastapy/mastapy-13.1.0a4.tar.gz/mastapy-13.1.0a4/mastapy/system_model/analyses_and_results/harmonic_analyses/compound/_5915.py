"""BeltDriveCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _6003
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "BeltDriveCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5715
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5946,
        _5905,
        _5984,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="BeltDriveCompoundHarmonicAnalysis")


class BeltDriveCompoundHarmonicAnalysis(
    _6003.SpecialisedAssemblyCompoundHarmonicAnalysis
):
    """BeltDriveCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveCompoundHarmonicAnalysis")

    class _Cast_BeltDriveCompoundHarmonicAnalysis:
        """Special nested class for casting BeltDriveCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
            parent: "BeltDriveCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_6003.SpecialisedAssemblyCompoundHarmonicAnalysis":
            return self._parent._cast(_6003.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_5905.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5905,
            )

            return self._parent._cast(_5905.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_5984.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5984,
            )

            return self._parent._cast(_5984.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_harmonic_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "_5946.CVTCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(_5946.CVTCompoundHarmonicAnalysis)

        @property
        def belt_drive_compound_harmonic_analysis(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
        ) -> "BeltDriveCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5715.BeltDriveHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_5715.BeltDriveHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.BeltDriveHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveCompoundHarmonicAnalysis._Cast_BeltDriveCompoundHarmonicAnalysis":
        return self._Cast_BeltDriveCompoundHarmonicAnalysis(self)
