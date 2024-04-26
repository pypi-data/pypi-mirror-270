"""GearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "GearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6921,
        _6841,
        _6850,
        _6855,
        _6869,
        _6873,
        _6890,
        _6912,
        _6933,
        _6940,
        _6943,
        _6946,
        _6981,
        _6987,
        _6990,
        _7010,
        _7013,
        _6876,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshLoadCase",)


Self = TypeVar("Self", bound="GearMeshLoadCase")


class GearMeshLoadCase(_6938.InterMountableComponentConnectionLoadCase):
    """GearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshLoadCase")

    class _Cast_GearMeshLoadCase:
        """Special nested class for casting GearMeshLoadCase to subclasses."""

        def __init__(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase", parent: "GearMeshLoadCase"
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6938.InterMountableComponentConnectionLoadCase":
            return self._parent._cast(_6938.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6876.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6876

            return self._parent._cast(_6876.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6841.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6850.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6850

            return self._parent._cast(_6850.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6855.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.BevelGearMeshLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6869.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6869

            return self._parent._cast(_6869.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6873.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6873

            return self._parent._cast(_6873.ConicalGearMeshLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6890.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6912.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6912

            return self._parent._cast(_6912.FaceGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6933.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6940.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6940

            return self._parent._cast(
                _6940.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6943.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(
                _6943.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6946.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(
                _6946.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6981.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6981

            return self._parent._cast(_6981.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6987.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_6990.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.StraightBevelGearMeshLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_7010.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7010

            return self._parent._cast(_7010.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "_7013.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _7013

            return self._parent._cast(_7013.ZerolBevelGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "GearMeshLoadCase._Cast_GearMeshLoadCase",
        ) -> "GearMeshLoadCase":
            return self._parent

        def __getattr__(self: "GearMeshLoadCase._Cast_GearMeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumPowerForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_power_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_power_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumPowerForGearMeshToBeLoaded = value

    @property
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.MinimumTorqueForGearMeshToBeLoaded

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @minimum_torque_for_gear_mesh_to_be_loaded.setter
    @enforce_parameter_types
    def minimum_torque_for_gear_mesh_to_be_loaded(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.MinimumTorqueForGearMeshToBeLoaded = value

    @property
    def number_of_steps_for_one_tooth_pass(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfStepsForOneToothPass

        if temp is None:
            return 0

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
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

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

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6921.GearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.GearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "GearMeshLoadCase._Cast_GearMeshLoadCase":
        return self._Cast_GearMeshLoadCase(self)
