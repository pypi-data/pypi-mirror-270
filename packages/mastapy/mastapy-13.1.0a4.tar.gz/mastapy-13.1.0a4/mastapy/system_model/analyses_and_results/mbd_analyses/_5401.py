"""AbstractShaftOrHousingMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5428
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AbstractShaftOrHousingMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2454
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5400,
        _5448,
        _5459,
        _5510,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingMultibodyDynamicsAnalysis")


class AbstractShaftOrHousingMultibodyDynamicsAnalysis(
    _5428.ComponentMultibodyDynamicsAnalysis
):
    """AbstractShaftOrHousingMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftOrHousingMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
            parent: "AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5400.AbstractShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5448.CycloidalDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5448

            return self._parent._cast(_5448.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5459.FEPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(_5459.FEPartMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "_5510.ShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(_5510.ShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftOrHousingMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_time_step(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumTimeStep

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_rigid_body_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfRigidBodyDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def component_design(self: Self) -> "_2454.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

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
    ) -> "AbstractShaftOrHousingMultibodyDynamicsAnalysis._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftOrHousingMultibodyDynamicsAnalysis(self)
