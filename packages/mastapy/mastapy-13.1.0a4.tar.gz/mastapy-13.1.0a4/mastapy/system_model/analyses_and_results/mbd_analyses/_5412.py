"""BeltDriveMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5513
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BeltDriveMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.static_loads import _6848
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5500,
        _5444,
        _5399,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BeltDriveMultibodyDynamicsAnalysis")


class BeltDriveMultibodyDynamicsAnalysis(
    _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
):
    """BeltDriveMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveMultibodyDynamicsAnalysis")

    class _Cast_BeltDriveMultibodyDynamicsAnalysis:
        """Special nested class for casting BeltDriveMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
            parent: "BeltDriveMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_5513.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5513.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_5399.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "_5444.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.CVTMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
        ) -> "BeltDriveMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "BeltDriveMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6848.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pulleys(self: Self) -> "List[_5500.PulleyMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PulleyMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Pulleys

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltDriveMultibodyDynamicsAnalysis._Cast_BeltDriveMultibodyDynamicsAnalysis":
        return self._Cast_BeltDriveMultibodyDynamicsAnalysis(self)
