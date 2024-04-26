"""MassDiscMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "MassDiscMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2480
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5488,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("MassDiscMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MassDiscMultibodyDynamicsAnalysis")


class MassDiscMultibodyDynamicsAnalysis(
    _5540.VirtualComponentMultibodyDynamicsAnalysis
):
    """MassDiscMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MassDiscMultibodyDynamicsAnalysis")

    class _Cast_MassDiscMultibodyDynamicsAnalysis:
        """Special nested class for casting MassDiscMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
            parent: "MassDiscMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_5540.VirtualComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5540.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
        ) -> "MassDiscMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "MassDiscMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2480.MassDisc":
        """mastapy.system_model.part_model.MassDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6948.MassDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MassDiscLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[MassDiscMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.MassDiscMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MassDiscMultibodyDynamicsAnalysis._Cast_MassDiscMultibodyDynamicsAnalysis":
        return self._Cast_MassDiscMultibodyDynamicsAnalysis(self)
