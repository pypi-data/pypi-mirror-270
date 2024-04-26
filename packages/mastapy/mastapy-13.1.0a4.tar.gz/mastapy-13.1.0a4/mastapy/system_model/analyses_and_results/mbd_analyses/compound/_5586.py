"""ConceptGearSetCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5615
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "ConceptGearSetCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5434
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5584,
        _5585,
        _5653,
        _5555,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearSetCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ConceptGearSetCompoundMultibodyDynamicsAnalysis")


class ConceptGearSetCompoundMultibodyDynamicsAnalysis(
    _5615.GearSetCompoundMultibodyDynamicsAnalysis
):
    """ConceptGearSetCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ConceptGearSetCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
            parent: "ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_compound_multibody_dynamics_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5615.GearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5615.GearSetCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_set_compound_multibody_dynamics_analysis(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
        ) -> "ConceptGearSetCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "ConceptGearSetCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2540.ConceptGearSet":
        """mastapy.system_model.part_model.gears.ConceptGearSet

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
    ) -> "List[_5434.ConceptGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptGearSetMultibodyDynamicsAnalysis]

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
    def concept_gears_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5584.ConceptGearCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptGearsCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def concept_meshes_compound_multibody_dynamics_analysis(
        self: Self,
    ) -> "List[_5585.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.compound.ConceptGearMeshCompoundMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConceptMeshesCompoundMultibodyDynamicsAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5434.ConceptGearSetMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ConceptGearSetMultibodyDynamicsAnalysis]

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
    ) -> "ConceptGearSetCompoundMultibodyDynamicsAnalysis._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ConceptGearSetCompoundMultibodyDynamicsAnalysis(self)
