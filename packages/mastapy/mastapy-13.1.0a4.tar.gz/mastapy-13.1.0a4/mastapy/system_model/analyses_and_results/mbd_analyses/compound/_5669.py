"""SynchroniserHalfCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5670
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2627
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5529
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5594,
        _5632,
        _5580,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfCompoundMultibodyDynamicsAnalysis")


class SynchroniserHalfCompoundMultibodyDynamicsAnalysis(
    _5670.SynchroniserPartCompoundMultibodyDynamicsAnalysis
):
    """SynchroniserHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserHalfCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
            parent: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5670.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5670.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5594.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5594,
            )

            return self._parent._cast(
                _5594.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
        ) -> "SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "SynchroniserHalfCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2627.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "List[_5529.SynchroniserHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserHalfMultibodyDynamicsAnalysis]

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
    ) -> "List[_5529.SynchroniserHalfMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.SynchroniserHalfMultibodyDynamicsAnalysis]

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
    ) -> "SynchroniserHalfCompoundMultibodyDynamicsAnalysis._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserHalfCompoundMultibodyDynamicsAnalysis(self)
