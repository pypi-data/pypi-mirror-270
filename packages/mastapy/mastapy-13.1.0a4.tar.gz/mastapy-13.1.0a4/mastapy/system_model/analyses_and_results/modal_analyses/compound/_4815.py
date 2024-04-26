"""HypoidGearSetCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4757
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "HypoidGearSetCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2553
    from mastapy.system_model.analyses_and_results.modal_analyses import _4664
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4813,
        _4814,
        _4785,
        _4811,
        _4849,
        _4751,
        _4830,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearSetCompoundModalAnalysis",)


Self = TypeVar("Self", bound="HypoidGearSetCompoundModalAnalysis")


class HypoidGearSetCompoundModalAnalysis(
    _4757.AGMAGleasonConicalGearSetCompoundModalAnalysis
):
    """HypoidGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearSetCompoundModalAnalysis")

    class _Cast_HypoidGearSetCompoundModalAnalysis:
        """Special nested class for casting HypoidGearSetCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
            parent: "HypoidGearSetCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4757.AGMAGleasonConicalGearSetCompoundModalAnalysis":
            return self._parent._cast(
                _4757.AGMAGleasonConicalGearSetCompoundModalAnalysis
            )

        @property
        def conical_gear_set_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4785.ConicalGearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4785,
            )

            return self._parent._cast(_4785.ConicalGearSetCompoundModalAnalysis)

        @property
        def gear_set_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4811.GearSetCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4811,
            )

            return self._parent._cast(_4811.GearSetCompoundModalAnalysis)

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4849.SpecialisedAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4751.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4751,
            )

            return self._parent._cast(_4751.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_4830.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4830,
            )

            return self._parent._cast(_4830.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_set_compound_modal_analysis(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
        ) -> "HypoidGearSetCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "HypoidGearSetCompoundModalAnalysis.TYPE"
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
    ) -> "List[_4664.HypoidGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis]

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
    def hypoid_gears_compound_modal_analysis(
        self: Self,
    ) -> "List[_4813.HypoidGearCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearsCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def hypoid_meshes_compound_modal_analysis(
        self: Self,
    ) -> "List[_4814.HypoidGearMeshCompoundModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.compound.HypoidGearMeshCompoundModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidMeshesCompoundModalAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4664.HypoidGearSetModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.HypoidGearSetModalAnalysis]

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
    ) -> "HypoidGearSetCompoundModalAnalysis._Cast_HypoidGearSetCompoundModalAnalysis":
        return self._Cast_HypoidGearSetCompoundModalAnalysis(self)
