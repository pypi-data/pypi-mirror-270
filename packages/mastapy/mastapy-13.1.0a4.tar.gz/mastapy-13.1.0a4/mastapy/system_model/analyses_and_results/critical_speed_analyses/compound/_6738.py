"""CouplingCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6799,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "CouplingCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6607
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6722,
        _6727,
        _6781,
        _6803,
        _6818,
        _6701,
        _6780,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="CouplingCompoundCriticalSpeedAnalysis")


class CouplingCompoundCriticalSpeedAnalysis(
    _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
):
    """CouplingCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CouplingCompoundCriticalSpeedAnalysis"
    )

    class _Cast_CouplingCompoundCriticalSpeedAnalysis:
        """Special nested class for casting CouplingCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
            parent: "CouplingCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6799.SpecialisedAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def abstract_assembly_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6701.AbstractAssemblyCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6701,
            )

            return self._parent._cast(
                _6701.AbstractAssemblyCompoundCriticalSpeedAnalysis
            )

        @property
        def part_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6780.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6780,
            )

            return self._parent._cast(_6780.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6722.ClutchCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.ClutchCompoundCriticalSpeedAnalysis)

        @property
        def concept_coupling_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6727.ConceptCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.ConceptCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def part_to_part_shear_coupling_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6781.PartToPartShearCouplingCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6781,
            )

            return self._parent._cast(
                _6781.PartToPartShearCouplingCompoundCriticalSpeedAnalysis
            )

        @property
        def spring_damper_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6803.SpringDamperCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(_6803.SpringDamperCompoundCriticalSpeedAnalysis)

        @property
        def torque_converter_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "_6818.TorqueConverterCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6818,
            )

            return self._parent._cast(
                _6818.TorqueConverterCompoundCriticalSpeedAnalysis
            )

        @property
        def coupling_compound_critical_speed_analysis(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
        ) -> "CouplingCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "CouplingCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6607.CouplingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingCriticalSpeedAnalysis]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6607.CouplingCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.CouplingCriticalSpeedAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "CouplingCompoundCriticalSpeedAnalysis._Cast_CouplingCompoundCriticalSpeedAnalysis":
        return self._Cast_CouplingCompoundCriticalSpeedAnalysis(self)
