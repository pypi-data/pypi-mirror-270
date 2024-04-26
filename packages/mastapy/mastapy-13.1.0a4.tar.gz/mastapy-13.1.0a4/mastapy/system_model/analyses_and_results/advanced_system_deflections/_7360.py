"""GearMeshAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7366
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "GearMeshAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.math_utility import _1525
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7304,
        _7311,
        _7316,
        _7329,
        _7332,
        _7348,
        _7355,
        _7364,
        _7368,
        _7371,
        _7374,
        _7402,
        _7408,
        _7411,
        _7427,
        _7430,
        _7334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="GearMeshAdvancedSystemDeflection")


class GearMeshAdvancedSystemDeflection(
    _7366.InterMountableComponentConnectionAdvancedSystemDeflection
):
    """GearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshAdvancedSystemDeflection")

    class _Cast_GearMeshAdvancedSystemDeflection:
        """Special nested class for casting GearMeshAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
            parent: "GearMeshAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7366.InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent._cast(
                _7366.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7334.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7304.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(
                _7304.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7311.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(
                _7311.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7316.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.BevelGearMeshAdvancedSystemDeflection)

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7329.ConceptGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7332.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7348.CylindricalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(_7348.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7355.FaceGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.FaceGearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7364.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7368.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(
                _7368.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7371.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(
                _7371.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> (
            "_7374.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7374,
            )

            return self._parent._cast(
                _7374.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7402.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7408.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(
                _7408.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7411.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(
                _7411.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7427.WormGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7427,
            )

            return self._parent._cast(_7427.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "_7430.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7430,
            )

            return self._parent._cast(_7430.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
        ) -> "GearMeshAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def mean_moment_about_centre_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanMomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_left_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationLeftFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_separation_right_flank(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumSeparationRightFlank

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_teeth_passed(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfTeethPassed

        if temp is None:
            return 0.0

        return temp

    @number_of_teeth_passed.setter
    @enforce_parameter_types
    def number_of_teeth_passed(self: Self, value: "float"):
        self.wrapped.NumberOfTeethPassed = float(value) if value is not None else 0.0

    @property
    def operating_total_contact_ratio_for_first_tooth_passing_period(
        self: Self,
    ) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OperatingTotalContactRatioForFirstToothPassingPeriod

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_moment_about_centre_from_ltca(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakMomentAboutCentreFromLTCA

        if temp is None:
            return 0.0

        return temp

    @property
    def peak_to_peak_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PeakToPeakMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def signed_root_mean_square_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SignedRootMeanSquareMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2331.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def misalignment_fourier_series_for_first_tooth_passing_period(
        self: Self,
    ) -> "_1525.FourierSeries":
        """mastapy.math_utility.FourierSeries

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MisalignmentFourierSeriesForFirstToothPassingPeriod

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshAdvancedSystemDeflection._Cast_GearMeshAdvancedSystemDeflection":
        return self._Cast_GearMeshAdvancedSystemDeflection(self)
