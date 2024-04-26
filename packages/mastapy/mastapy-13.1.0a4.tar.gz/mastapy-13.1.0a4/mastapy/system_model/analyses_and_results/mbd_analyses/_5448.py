"""CycloidalDiscMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CycloidalDiscMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2587
    from mastapy.system_model.analyses_and_results.static_loads import _6886
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5401,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CycloidalDiscMultibodyDynamicsAnalysis")


class CycloidalDiscMultibodyDynamicsAnalysis(
    _5400.AbstractShaftMultibodyDynamicsAnalysis
):
    """CycloidalDiscMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscMultibodyDynamicsAnalysis"
    )

    class _Cast_CycloidalDiscMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5400.AbstractShaftMultibodyDynamicsAnalysis":
            return self._parent._cast(_5400.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def component_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CycloidalDiscMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2587.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6886.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "CycloidalDiscMultibodyDynamicsAnalysis._Cast_CycloidalDiscMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscMultibodyDynamicsAnalysis(self)
