"""PlanetaryGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3969
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "PlanetaryGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3872
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3980,
        _4018,
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundStabilityAnalysis")


class PlanetaryGearSetCompoundStabilityAnalysis(
    _3969.CylindricalGearSetCompoundStabilityAnalysis
):
    """PlanetaryGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryGearSetCompoundStabilityAnalysis"
    )

    class _Cast_PlanetaryGearSetCompoundStabilityAnalysis:
        """Special nested class for casting PlanetaryGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
            parent: "PlanetaryGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3969.CylindricalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(_3969.CylindricalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_stability_analysis(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
        ) -> "PlanetaryGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3872.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3872.PlanetaryGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.PlanetaryGearSetStabilityAnalysis]

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
    ) -> "PlanetaryGearSetCompoundStabilityAnalysis._Cast_PlanetaryGearSetCompoundStabilityAnalysis":
        return self._Cast_PlanetaryGearSetCompoundStabilityAnalysis(self)
