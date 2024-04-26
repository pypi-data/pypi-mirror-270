"""PartToPartShearCouplingHalfMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfMultibodyDynamicsAnalysis")


class PartToPartShearCouplingHalfMultibodyDynamicsAnalysis(
    _5441.CouplingHalfMultibodyDynamicsAnalysis
):
    """PartToPartShearCouplingHalfMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
            parent: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5441.CouplingHalfMultibodyDynamicsAnalysis":
            return self._parent._cast(_5441.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
        ) -> "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6957.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalfMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
        return self._Cast_PartToPartShearCouplingHalfMultibodyDynamicsAnalysis(self)
