"""InterMountableComponentConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7334
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "InterMountableComponentConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7304,
        _7308,
        _7311,
        _7316,
        _7321,
        _7326,
        _7329,
        _7332,
        _7338,
        _7341,
        _7348,
        _7355,
        _7360,
        _7364,
        _7368,
        _7371,
        _7374,
        _7383,
        _7392,
        _7395,
        _7402,
        _7405,
        _7408,
        _7411,
        _7420,
        _7427,
        _7430,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="InterMountableComponentConnectionAdvancedSystemDeflection"
)


class InterMountableComponentConnectionAdvancedSystemDeflection(
    _7334.ConnectionAdvancedSystemDeflection
):
    """InterMountableComponentConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
    )

    class _Cast_InterMountableComponentConnectionAdvancedSystemDeflection:
        """Special nested class for casting InterMountableComponentConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
            parent: "InterMountableComponentConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7334.ConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7334.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7304.AGMAGleasonConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7304,
            )

            return self._parent._cast(
                _7304.AGMAGleasonConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7308.BeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7308,
            )

            return self._parent._cast(_7308.BeltConnectionAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7311.BevelDifferentialGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7311,
            )

            return self._parent._cast(
                _7311.BevelDifferentialGearMeshAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7316.BevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7316,
            )

            return self._parent._cast(_7316.BevelGearMeshAdvancedSystemDeflection)

        @property
        def clutch_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7321.ClutchConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7321,
            )

            return self._parent._cast(_7321.ClutchConnectionAdvancedSystemDeflection)

        @property
        def concept_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7326.ConceptCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7326,
            )

            return self._parent._cast(
                _7326.ConceptCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def concept_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7329.ConceptGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7329,
            )

            return self._parent._cast(_7329.ConceptGearMeshAdvancedSystemDeflection)

        @property
        def conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7332.ConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7332,
            )

            return self._parent._cast(_7332.ConicalGearMeshAdvancedSystemDeflection)

        @property
        def coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7338.CouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7338,
            )

            return self._parent._cast(_7338.CouplingConnectionAdvancedSystemDeflection)

        @property
        def cvt_belt_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7341.CVTBeltConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7341,
            )

            return self._parent._cast(_7341.CVTBeltConnectionAdvancedSystemDeflection)

        @property
        def cylindrical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7348.CylindricalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(_7348.CylindricalGearMeshAdvancedSystemDeflection)

        @property
        def face_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7355.FaceGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.FaceGearMeshAdvancedSystemDeflection)

        @property
        def gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7360.GearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7360,
            )

            return self._parent._cast(_7360.GearMeshAdvancedSystemDeflection)

        @property
        def hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7364.HypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7364,
            )

            return self._parent._cast(_7364.HypoidGearMeshAdvancedSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7368.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7368,
            )

            return self._parent._cast(
                _7368.KlingelnbergCycloPalloidConicalGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7371.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7371,
            )

            return self._parent._cast(
                _7371.KlingelnbergCycloPalloidHypoidGearMeshAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
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
        def part_to_part_shear_coupling_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7383.PartToPartShearCouplingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7383,
            )

            return self._parent._cast(
                _7383.PartToPartShearCouplingConnectionAdvancedSystemDeflection
            )

        @property
        def ring_pins_to_disc_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7392.RingPinsToDiscConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7392,
            )

            return self._parent._cast(
                _7392.RingPinsToDiscConnectionAdvancedSystemDeflection
            )

        @property
        def rolling_ring_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7395.RollingRingConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7395,
            )

            return self._parent._cast(
                _7395.RollingRingConnectionAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7402.SpiralBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7402,
            )

            return self._parent._cast(_7402.SpiralBevelGearMeshAdvancedSystemDeflection)

        @property
        def spring_damper_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7405.SpringDamperConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7405,
            )

            return self._parent._cast(
                _7405.SpringDamperConnectionAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7408.StraightBevelDiffGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7408,
            )

            return self._parent._cast(
                _7408.StraightBevelDiffGearMeshAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7411.StraightBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7411,
            )

            return self._parent._cast(
                _7411.StraightBevelGearMeshAdvancedSystemDeflection
            )

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7420.TorqueConverterConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7420,
            )

            return self._parent._cast(
                _7420.TorqueConverterConnectionAdvancedSystemDeflection
            )

        @property
        def worm_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7427.WormGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7427,
            )

            return self._parent._cast(_7427.WormGearMeshAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_mesh_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "_7430.ZerolBevelGearMeshAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7430,
            )

            return self._parent._cast(_7430.ZerolBevelGearMeshAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
        ) -> "InterMountableComponentConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "InterMountableComponentConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2299.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionAdvancedSystemDeflection._Cast_InterMountableComponentConnectionAdvancedSystemDeflection":
        return self._Cast_InterMountableComponentConnectionAdvancedSystemDeflection(
            self
        )
