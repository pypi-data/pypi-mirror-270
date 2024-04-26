"""AGMAGleasonConicalGearSetDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.gear_designs.bevel import _1189
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.conical import _1166
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalGearSetDesign",
)

if TYPE_CHECKING:
    from mastapy.gleason_smt_link import _312
    from mastapy.gears import _352, _355
    from mastapy.gears.gear_designs.conical import _1175
    from mastapy.gears.gear_designs.agma_gleason_conical import _1204
    from mastapy.gears.gear_designs.zerol_bevel import _962
    from mastapy.gears.gear_designs.straight_bevel import _971
    from mastapy.gears.gear_designs.straight_bevel_diff import _975
    from mastapy.gears.gear_designs.spiral_bevel import _979
    from mastapy.gears.gear_designs.hypoid import _995
    from mastapy.gears.gear_designs.bevel import _1192
    from mastapy.gears.gear_designs import _958, _956


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetDesign")


class AGMAGleasonConicalGearSetDesign(_1166.ConicalGearSetDesign):
    """AGMAGleasonConicalGearSetDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetDesign")

    class _Cast_AGMAGleasonConicalGearSetDesign:
        """Special nested class for casting AGMAGleasonConicalGearSetDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
            parent: "AGMAGleasonConicalGearSetDesign",
        ):
            self._parent = parent

        @property
        def conical_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_1166.ConicalGearSetDesign":
            return self._parent._cast(_1166.ConicalGearSetDesign)

        @property
        def gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_958.GearSetDesign":
            from mastapy.gears.gear_designs import _958

            return self._parent._cast(_958.GearSetDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_956.GearDesignComponent":
            from mastapy.gears.gear_designs import _956

            return self._parent._cast(_956.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_962.ZerolBevelGearSetDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _962

            return self._parent._cast(_962.ZerolBevelGearSetDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_971.StraightBevelGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel import _971

            return self._parent._cast(_971.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_975.StraightBevelDiffGearSetDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _975

            return self._parent._cast(_975.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_979.SpiralBevelGearSetDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _979

            return self._parent._cast(_979.SpiralBevelGearSetDesign)

        @property
        def hypoid_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_995.HypoidGearSetDesign":
            from mastapy.gears.gear_designs.hypoid import _995

            return self._parent._cast(_995.HypoidGearSetDesign)

        @property
        def bevel_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "_1192.BevelGearSetDesign":
            from mastapy.gears.gear_designs.bevel import _1192

            return self._parent._cast(_1192.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
        ) -> "AGMAGleasonConicalGearSetDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AGMAGleasonConicalGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crown_gear_to_cutter_centre_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CrownGearToCutterCentreDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def design_method(
        self: Self,
    ) -> "enum_with_selected_value.EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods":
        """EnumWithSelectedValue[mastapy.gears.gear_designs.bevel.AGMAGleasonConicalGearGeometryMethods]"""
        temp = self.wrapped.DesignMethod

        if temp is None:
            return None

        value = (
            enum_with_selected_value.EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods.wrapped_type()
        )
        return enum_with_selected_value_runtime.create(temp, value)

    @design_method.setter
    @enforce_parameter_types
    def design_method(self: Self, value: "_1189.AGMAGleasonConicalGearGeometryMethods"):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = (
            enum_with_selected_value.EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods.implicit_type()
        )
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DesignMethod = value

    @property
    def epicycloid_base_circle_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EpicycloidBaseCircleRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_minimum_factor_of_safety_bending(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GleasonMinimumFactorOfSafetyBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gleason_minimum_factor_of_safety_bending.setter
    @enforce_parameter_types
    def gleason_minimum_factor_of_safety_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GleasonMinimumFactorOfSafetyBending = value

    @property
    def gleason_minimum_factor_of_safety_contact(
        self: Self,
    ) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.GleasonMinimumFactorOfSafetyContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @gleason_minimum_factor_of_safety_contact.setter
    @enforce_parameter_types
    def gleason_minimum_factor_of_safety_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.GleasonMinimumFactorOfSafetyContact = value

    @property
    def input_module(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.InputModule

        if temp is None:
            return False

        return temp

    @input_module.setter
    @enforce_parameter_types
    def input_module(self: Self, value: "bool"):
        self.wrapped.InputModule = bool(value) if value is not None else False

    @property
    def manufacturing_method(self: Self) -> "_312.CutterMethod":
        """mastapy.gleason_smt_link.CutterMethod"""
        temp = self.wrapped.ManufacturingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.GleasonSMTLink.CutterMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gleason_smt_link._312", "CutterMethod"
        )(value)

    @manufacturing_method.setter
    @enforce_parameter_types
    def manufacturing_method(self: Self, value: "_312.CutterMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.GleasonSMTLink.CutterMethod"
        )
        self.wrapped.ManufacturingMethod = value

    @property
    def mean_normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanNormalModule

        if temp is None:
            return 0.0

        return temp

    @mean_normal_module.setter
    @enforce_parameter_types
    def mean_normal_module(self: Self, value: "float"):
        self.wrapped.MeanNormalModule = float(value) if value is not None else 0.0

    @property
    def number_of_blade_groups(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfBladeGroups

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_crown_gear_teeth(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfCrownGearTeeth

        if temp is None:
            return 0.0

        return temp

    @property
    def pinion_offset_angle_in_root_plane(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionOffsetAngleInRootPlane

        if temp is None:
            return 0.0

        return temp

    @property
    def pitch_limit_pressure_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchLimitPressureAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def reliability_factor_bending(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ReliabilityFactorBending

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @reliability_factor_bending.setter
    @enforce_parameter_types
    def reliability_factor_bending(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ReliabilityFactorBending = value

    @property
    def reliability_factor_contact(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.ReliabilityFactorContact

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @reliability_factor_contact.setter
    @enforce_parameter_types
    def reliability_factor_contact(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.ReliabilityFactorContact = value

    @property
    def reliability_requirement_agma(self: Self) -> "_352.SafetyRequirementsAGMA":
        """mastapy.gears.SafetyRequirementsAGMA"""
        temp = self.wrapped.ReliabilityRequirementAGMA

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._352", "SafetyRequirementsAGMA"
        )(value)

    @reliability_requirement_agma.setter
    @enforce_parameter_types
    def reliability_requirement_agma(self: Self, value: "_352.SafetyRequirementsAGMA"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SafetyRequirementsAGMA"
        )
        self.wrapped.ReliabilityRequirementAGMA = value

    @property
    def reliability_requirement_gleason(
        self: Self,
    ) -> "_1175.GleasonSafetyRequirements":
        """mastapy.gears.gear_designs.conical.GleasonSafetyRequirements"""
        temp = self.wrapped.ReliabilityRequirementGleason

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.GearDesigns.Conical.GleasonSafetyRequirements"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears.gear_designs.conical._1175", "GleasonSafetyRequirements"
        )(value)

    @reliability_requirement_gleason.setter
    @enforce_parameter_types
    def reliability_requirement_gleason(
        self: Self, value: "_1175.GleasonSafetyRequirements"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.GearDesigns.Conical.GleasonSafetyRequirements"
        )
        self.wrapped.ReliabilityRequirementGleason = value

    @property
    def required_minimum_topland_to_module_factor(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RequiredMinimumToplandToModuleFactor

        if temp is None:
            return 0.0

        return temp

    @required_minimum_topland_to_module_factor.setter
    @enforce_parameter_types
    def required_minimum_topland_to_module_factor(self: Self, value: "float"):
        self.wrapped.RequiredMinimumToplandToModuleFactor = (
            float(value) if value is not None else 0.0
        )

    @property
    def tooth_taper(self: Self) -> "_355.SpiralBevelToothTaper":
        """mastapy.gears.SpiralBevelToothTaper"""
        temp = self.wrapped.ToothTaper

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.SpiralBevelToothTaper"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._355", "SpiralBevelToothTaper"
        )(value)

    @tooth_taper.setter
    @enforce_parameter_types
    def tooth_taper(self: Self, value: "_355.SpiralBevelToothTaper"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.SpiralBevelToothTaper"
        )
        self.wrapped.ToothTaper = value

    @property
    def wheel_involute_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInvoluteConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_involute_to_mean_cone_distance_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInvoluteToMeanConeDistanceRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_involute_to_outer_cone_distance_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelInvoluteToOuterConeDistanceRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def conical_meshes(self: Self) -> "List[_1204.AGMAGleasonConicalGearMeshDesign]":
        """List[mastapy.gears.gear_designs.agma_gleason_conical.AGMAGleasonConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def meshes(self: Self) -> "List[_1204.AGMAGleasonConicalGearMeshDesign]":
        """List[mastapy.gears.gear_designs.agma_gleason_conical.AGMAGleasonConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Meshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def export_ki_mo_skip_file(self: Self):
        """Method does not return."""
        self.wrapped.ExportKIMoSKIPFile()

    def gleason_gemsxml_data(self: Self):
        """Method does not return."""
        self.wrapped.GleasonGEMSXMLData()

    def ki_mo_sxml_data(self: Self):
        """Method does not return."""
        self.wrapped.KIMoSXMLData()

    def store_ki_mo_skip_file(self: Self):
        """Method does not return."""
        self.wrapped.StoreKIMoSKIPFile()

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetDesign._Cast_AGMAGleasonConicalGearSetDesign":
        return self._Cast_AGMAGleasonConicalGearSetDesign(self)
