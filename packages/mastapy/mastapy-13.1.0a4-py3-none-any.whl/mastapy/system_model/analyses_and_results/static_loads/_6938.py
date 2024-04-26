"""InterMountableComponentConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6876
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2299
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6841,
        _6847,
        _6850,
        _6855,
        _6859,
        _6865,
        _6869,
        _6873,
        _6878,
        _6881,
        _6890,
        _6912,
        _6919,
        _6933,
        _6940,
        _6943,
        _6946,
        _6956,
        _6971,
        _6973,
        _6981,
        _6983,
        _6987,
        _6990,
        _6999,
        _7010,
        _7013,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionLoadCase")


class InterMountableComponentConnectionLoadCase(_6876.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionLoadCase"
    )

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
            parent: "InterMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6841.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6847.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6850.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6855.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6859.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6865.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6865

            return self._parent._cast(_6865.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6869.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6869

            return self._parent._cast(_6869.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6873.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6878.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6878

            return self._parent._cast(_6878.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6881.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6881

            return self._parent._cast(_6881.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6890.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6912.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6919.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(_6919.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6933.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6940.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(
                _6940.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6943.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(
                _6943.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6946.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(
                _6946.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6956.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6971.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6973.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6981.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6983.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6987.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6990.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6999.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6999

            return self._parent._cast(_6999.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_7010.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7010

            return self._parent._cast(_7010.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_7013.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7013

            return self._parent._cast(_7013.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "InterMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

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
    ) -> "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase":
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
