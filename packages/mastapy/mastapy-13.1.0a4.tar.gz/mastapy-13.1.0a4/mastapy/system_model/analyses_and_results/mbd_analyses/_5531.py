"""SynchroniserPartMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "SynchroniserPartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2628
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5529,
        _5532,
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartMultibodyDynamicsAnalysis")


class SynchroniserPartMultibodyDynamicsAnalysis(
    _5441.CouplingHalfMultibodyDynamicsAnalysis
):
    """SynchroniserPartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartMultibodyDynamicsAnalysis"
    )

    class _Cast_SynchroniserPartMultibodyDynamicsAnalysis:
        """Special nested class for casting SynchroniserPartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
            parent: "SynchroniserPartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5529.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5529

            return self._parent._cast(_5529.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "_5532.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5532

            return self._parent._cast(_5532.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
        ) -> "SynchroniserPartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2628.SynchroniserPart":
        """mastapy.system_model.part_model.couplings.SynchroniserPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartMultibodyDynamicsAnalysis._Cast_SynchroniserPartMultibodyDynamicsAnalysis":
        return self._Cast_SynchroniserPartMultibodyDynamicsAnalysis(self)
