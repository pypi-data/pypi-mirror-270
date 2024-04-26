"""CVTMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5412
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "CVTMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5513,
        _5399,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTMultibodyDynamicsAnalysis")


class CVTMultibodyDynamicsAnalysis(_5412.BeltDriveMultibodyDynamicsAnalysis):
    """CVTMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTMultibodyDynamicsAnalysis")

    class _Cast_CVTMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            parent: "CVTMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5412.BeltDriveMultibodyDynamicsAnalysis":
            return self._parent._cast(_5412.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
        ) -> "CVTMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTMultibodyDynamicsAnalysis._Cast_CVTMultibodyDynamicsAnalysis":
        return self._Cast_CVTMultibodyDynamicsAnalysis(self)
