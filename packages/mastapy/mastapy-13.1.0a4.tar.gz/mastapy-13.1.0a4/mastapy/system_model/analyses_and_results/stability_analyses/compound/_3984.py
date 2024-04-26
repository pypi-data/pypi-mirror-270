"""HypoidGearSetCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "HypoidGearSetCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.stability_analyses import _3851
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3982,
        _3983,
        _3954,
        _3980,
        _4018,
        _3920,
        _3999,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundStabilityAnalysis")


class HypoidGearSetCompoundStabilityAnalysis(
    _3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
):
    """HypoidGearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearSetCompoundStabilityAnalysis"
    )

    class _Cast_HypoidGearSetCompoundStabilityAnalysis:
        """Special nested class for casting HypoidGearSetCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
            parent: "HypoidGearSetCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis":
            return self._parent._cast(
                _3926.AGMAGleasonConicalGearSetCompoundStabilityAnalysis
            )

        @property
        def conical_gear_set_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3954.ConicalGearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3954,
            )

            return self._parent._cast(_3954.ConicalGearSetCompoundStabilityAnalysis)

        @property
        def gear_set_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3980.GearSetCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3980,
            )

            return self._parent._cast(_3980.GearSetCompoundStabilityAnalysis)

        @property
        def specialised_assembly_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_4018.SpecialisedAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4018,
            )

            return self._parent._cast(
                _4018.SpecialisedAssemblyCompoundStabilityAnalysis
            )

        @property
        def abstract_assembly_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3920.AbstractAssemblyCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3920,
            )

            return self._parent._cast(_3920.AbstractAssemblyCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_3999.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3999,
            )

            return self._parent._cast(_3999.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_stability_analysis(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
        ) -> "HypoidGearSetCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearSetCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2553.HypoidGearSet":
        """mastapy.system_model.part_model.gears.HypoidGearSet

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
    ) -> "List[_3851.HypoidGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearSetStabilityAnalysis]

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
    def hypoid_gears_compound_stability_analysis(
        self: Self,
    ) -> "List[_3982.HypoidGearCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.HypoidGearCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_stability_analysis(
        self: Self,
    ) -> "List[_3983.HypoidGearMeshCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.HypoidGearMeshCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3851.HypoidGearSetStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.HypoidGearSetStabilityAnalysis]

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
    ) -> "HypoidGearSetCompoundStabilityAnalysis._Cast_HypoidGearSetCompoundStabilityAnalysis":
        return self._Cast_HypoidGearSetCompoundStabilityAnalysis(self)
