"""RootAssemblyCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "RootAssemblyCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5506
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5555,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="RootAssemblyCompoundMultibodyDynamicsAnalysis")


class RootAssemblyCompoundMultibodyDynamicsAnalysis(
    _5562.AssemblyCompoundMultibodyDynamicsAnalysis
):
    """RootAssemblyCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting RootAssemblyCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
            parent: "RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def assembly_compound_multibody_dynamics_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5562.AssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5562.AssemblyCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.AbstractAssemblyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5555,
            )

            return self._parent._cast(
                _5555.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def root_assembly_compound_multibody_dynamics_analysis(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
        ) -> "RootAssemblyCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "RootAssemblyCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5506.RootAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RootAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "List[_5506.RootAssemblyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.RootAssemblyMultibodyDynamicsAnalysis]

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
    ) -> "RootAssemblyCompoundMultibodyDynamicsAnalysis._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis":
        return self._Cast_RootAssemblyCompoundMultibodyDynamicsAnalysis(self)
