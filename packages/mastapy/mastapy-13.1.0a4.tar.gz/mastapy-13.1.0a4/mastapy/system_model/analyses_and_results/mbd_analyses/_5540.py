"""VirtualComponentMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5488
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "VirtualComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2497
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5483,
        _5487,
        _5498,
        _5499,
        _5539,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="VirtualComponentMultibodyDynamicsAnalysis")


class VirtualComponentMultibodyDynamicsAnalysis(
    _5488.MountableComponentMultibodyDynamicsAnalysis
):
    """VirtualComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentMultibodyDynamicsAnalysis"
    )

    class _Cast_VirtualComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting VirtualComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
            parent: "VirtualComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5488.MountableComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5488.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5483.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5487.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(
                _5487.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def point_load_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5498.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(_5498.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5499.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(_5499.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "_5539.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5539

            return self._parent._cast(_5539.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
        ) -> "VirtualComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "VirtualComponentMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def acceleration_translation_local_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AccelerationTranslationLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def displacement_translation_local_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DisplacementTranslationLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def velocity_translation_local_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VelocityTranslationLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def component_design(self: Self) -> "_2497.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentMultibodyDynamicsAnalysis._Cast_VirtualComponentMultibodyDynamicsAnalysis":
        return self._Cast_VirtualComponentMultibodyDynamicsAnalysis(self)
