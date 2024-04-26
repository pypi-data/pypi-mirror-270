"""PointLoadCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5677
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PointLoadCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2489
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5498
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5632,
        _5580,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PointLoadCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PointLoadCompoundMultibodyDynamicsAnalysis")


class PointLoadCompoundMultibodyDynamicsAnalysis(
    _5677.VirtualComponentCompoundMultibodyDynamicsAnalysis
):
    """PointLoadCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PointLoadCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_PointLoadCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PointLoadCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
            parent: "PointLoadCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_5677.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5677.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_5632.MountableComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5632,
            )

            return self._parent._cast(
                _5632.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
        ) -> "PointLoadCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "PointLoadCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2489.PointLoad":
        """mastapy.system_model.part_model.PointLoad

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
    ) -> "List[_5498.PointLoadMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PointLoadMultibodyDynamicsAnalysis]

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
    ) -> "List[_5498.PointLoadMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PointLoadMultibodyDynamicsAnalysis]

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
    ) -> "PointLoadCompoundMultibodyDynamicsAnalysis._Cast_PointLoadCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PointLoadCompoundMultibodyDynamicsAnalysis(self)
