"""ShaftMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ShaftMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2500
    from mastapy.system_model.analyses_and_results.static_loads import _6977
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5401,
        _5428,
        _5491,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7575, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ShaftMultibodyDynamicsAnalysis")


class ShaftMultibodyDynamicsAnalysis(_5400.AbstractShaftMultibodyDynamicsAnalysis):
    """ShaftMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftMultibodyDynamicsAnalysis")

    class _Cast_ShaftMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
            parent: "ShaftMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_5400.AbstractShaftMultibodyDynamicsAnalysis":
            return self._parent._cast(_5400.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(
                _5401.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def component_multibody_dynamics_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_5428.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(_5428.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_5491.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(_5491.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_7575.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7575

            return self._parent._cast(_7575.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
        ) -> "ShaftMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftMultibodyDynamicsAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_velocities(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AngularVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_acceleration_torques(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticAccelerationTorques

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_acceleration_x_force(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticAccelerationXForce

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_acceleration_y_force(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticAccelerationYForce

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_force_x(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticForceX

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_force_y(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticForceY

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_force_z(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticForceZ

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_x_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_x_velocities(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalXVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_y_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_y_velocities(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalYVelocities

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_z_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalZDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_theta_x_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalThetaXDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_local_theta_y_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticLocalThetaYDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_moment_x(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticMomentX

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_moment_y(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticMomentY

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_quadratic_velocity_torques(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticQuadraticVelocityTorques

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_quadratic_velocity_x_force(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticQuadraticVelocityXForce

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_quadratic_velocity_y_force(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticQuadraticVelocityYForce

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_radial_deflections(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticRadialDeflections

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_torques(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticTorques

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def elastic_twists(self: Self) -> "List[float]":
        """List[float]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElasticTwists

        if temp is None:
            return None

        value = conversion.to_list_any(temp)

        if value is None:
            return None

        return value

    @property
    def kinetic_energy(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KineticEnergy

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_acceleration_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceAccelerationTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_quadratic_velocity_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceQuadraticVelocityTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_translation_acceleration_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceTranslationAccelerationForce

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_translation_acceleration_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceTranslationAccelerationTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_translation_quadratic_velocity_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceTranslationQuadraticVelocityForce

        if temp is None:
            return 0.0

        return temp

    @property
    def reference_translation_quadratic_velocity_torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReferenceTranslationQuadraticVelocityTorque

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2500.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6977.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftMultibodyDynamicsAnalysis]

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
    ) -> "ShaftMultibodyDynamicsAnalysis._Cast_ShaftMultibodyDynamicsAnalysis":
        return self._Cast_ShaftMultibodyDynamicsAnalysis(self)
