"""Material"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.utility.databases import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL = python_net_import("SMT.MastaAPI.Materials", "Material")

if TYPE_CHECKING:
    from mastapy.materials import _265, _281, _252
    from mastapy.shafts import _24
    from mastapy.gears.materials import _590, _592, _594, _598, _601, _604, _608, _610
    from mastapy.electric_machines import _1295, _1313, _1326
    from mastapy.detailed_rigid_connectors.splines import _1428
    from mastapy.cycloidal import _1468, _1475
    from mastapy.bolts import _1478, _1482


__docformat__ = "restructuredtext en"
__all__ = ("Material",)


Self = TypeVar("Self", bound="Material")


class Material(_1844.NamedDatabaseItem):
    """Material

    This is a mastapy class.
    """

    TYPE = _MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Material")

    class _Cast_Material:
        """Special nested class for casting Material to subclasses."""

        def __init__(self: "Material._Cast_Material", parent: "Material"):
            self._parent = parent

        @property
        def named_database_item(
            self: "Material._Cast_Material",
        ) -> "_1844.NamedDatabaseItem":
            return self._parent._cast(_1844.NamedDatabaseItem)

        @property
        def shaft_material(self: "Material._Cast_Material") -> "_24.ShaftMaterial":
            from mastapy.shafts import _24

            return self._parent._cast(_24.ShaftMaterial)

        @property
        def bearing_material(self: "Material._Cast_Material") -> "_252.BearingMaterial":
            from mastapy.materials import _252

            return self._parent._cast(_252.BearingMaterial)

        @property
        def agma_cylindrical_gear_material(
            self: "Material._Cast_Material",
        ) -> "_590.AGMACylindricalGearMaterial":
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(
            self: "Material._Cast_Material",
        ) -> "_592.BevelGearISOMaterial":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.BevelGearISOMaterial)

        @property
        def bevel_gear_material(
            self: "Material._Cast_Material",
        ) -> "_594.BevelGearMaterial":
            from mastapy.gears.materials import _594

            return self._parent._cast(_594.BevelGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "Material._Cast_Material",
        ) -> "_598.CylindricalGearMaterial":
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.CylindricalGearMaterial)

        @property
        def gear_material(self: "Material._Cast_Material") -> "_601.GearMaterial":
            from mastapy.gears.materials import _601

            return self._parent._cast(_601.GearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "Material._Cast_Material",
        ) -> "_604.ISOCylindricalGearMaterial":
            from mastapy.gears.materials import _604

            return self._parent._cast(_604.ISOCylindricalGearMaterial)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "Material._Cast_Material",
        ) -> "_608.KlingelnbergCycloPalloidConicalGearMaterial":
            from mastapy.gears.materials import _608

            return self._parent._cast(_608.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "Material._Cast_Material",
        ) -> "_610.PlasticCylindricalGearMaterial":
            from mastapy.gears.materials import _610

            return self._parent._cast(_610.PlasticCylindricalGearMaterial)

        @property
        def magnet_material(self: "Material._Cast_Material") -> "_1295.MagnetMaterial":
            from mastapy.electric_machines import _1295

            return self._parent._cast(_1295.MagnetMaterial)

        @property
        def stator_rotor_material(
            self: "Material._Cast_Material",
        ) -> "_1313.StatorRotorMaterial":
            from mastapy.electric_machines import _1313

            return self._parent._cast(_1313.StatorRotorMaterial)

        @property
        def winding_material(
            self: "Material._Cast_Material",
        ) -> "_1326.WindingMaterial":
            from mastapy.electric_machines import _1326

            return self._parent._cast(_1326.WindingMaterial)

        @property
        def spline_material(self: "Material._Cast_Material") -> "_1428.SplineMaterial":
            from mastapy.detailed_rigid_connectors.splines import _1428

            return self._parent._cast(_1428.SplineMaterial)

        @property
        def cycloidal_disc_material(
            self: "Material._Cast_Material",
        ) -> "_1468.CycloidalDiscMaterial":
            from mastapy.cycloidal import _1468

            return self._parent._cast(_1468.CycloidalDiscMaterial)

        @property
        def ring_pins_material(
            self: "Material._Cast_Material",
        ) -> "_1475.RingPinsMaterial":
            from mastapy.cycloidal import _1475

            return self._parent._cast(_1475.RingPinsMaterial)

        @property
        def bolted_joint_material(
            self: "Material._Cast_Material",
        ) -> "_1478.BoltedJointMaterial":
            from mastapy.bolts import _1478

            return self._parent._cast(_1478.BoltedJointMaterial)

        @property
        def bolt_material(self: "Material._Cast_Material") -> "_1482.BoltMaterial":
            from mastapy.bolts import _1482

            return self._parent._cast(_1482.BoltMaterial)

        @property
        def material(self: "Material._Cast_Material") -> "Material":
            return self._parent

        def __getattr__(self: "Material._Cast_Material", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Material.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_thermal_expansion(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoefficientOfThermalExpansion

        if temp is None:
            return 0.0

        return temp

    @coefficient_of_thermal_expansion.setter
    @enforce_parameter_types
    def coefficient_of_thermal_expansion(self: Self, value: "float"):
        self.wrapped.CoefficientOfThermalExpansion = (
            float(value) if value is not None else 0.0
        )

    @property
    def cost_per_unit_mass(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CostPerUnitMass

        if temp is None:
            return 0.0

        return temp

    @cost_per_unit_mass.setter
    @enforce_parameter_types
    def cost_per_unit_mass(self: Self, value: "float"):
        self.wrapped.CostPerUnitMass = float(value) if value is not None else 0.0

    @property
    def density(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Density

        if temp is None:
            return 0.0

        return temp

    @density.setter
    @enforce_parameter_types
    def density(self: Self, value: "float"):
        self.wrapped.Density = float(value) if value is not None else 0.0

    @property
    def hardness_type(self: Self) -> "_265.HardnessType":
        """mastapy.materials.HardnessType"""
        temp = self.wrapped.HardnessType

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(temp, "SMT.MastaAPI.Materials.HardnessType")

        if value is None:
            return None

        return constructor.new_from_mastapy("mastapy.materials._265", "HardnessType")(
            value
        )

    @hardness_type.setter
    @enforce_parameter_types
    def hardness_type(self: Self, value: "_265.HardnessType"):
        value = conversion.mp_to_pn_enum(value, "SMT.MastaAPI.Materials.HardnessType")
        self.wrapped.HardnessType = value

    @property
    def heat_conductivity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.HeatConductivity

        if temp is None:
            return 0.0

        return temp

    @heat_conductivity.setter
    @enforce_parameter_types
    def heat_conductivity(self: Self, value: "float"):
        self.wrapped.HeatConductivity = float(value) if value is not None else 0.0

    @property
    def material_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaterialName

        if temp is None:
            return ""

        return temp

    @property
    def maximum_allowable_temperature(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MaximumAllowableTemperature

        if temp is None:
            return 0.0

        return temp

    @maximum_allowable_temperature.setter
    @enforce_parameter_types
    def maximum_allowable_temperature(self: Self, value: "float"):
        self.wrapped.MaximumAllowableTemperature = (
            float(value) if value is not None else 0.0
        )

    @property
    def modulus_of_elasticity(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ModulusOfElasticity

        if temp is None:
            return 0.0

        return temp

    @modulus_of_elasticity.setter
    @enforce_parameter_types
    def modulus_of_elasticity(self: Self, value: "float"):
        self.wrapped.ModulusOfElasticity = float(value) if value is not None else 0.0

    @property
    def plane_strain_modulus(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlaneStrainModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def poissons_ratio(self: Self) -> "float":
        """float"""
        temp = self.wrapped.PoissonsRatio

        if temp is None:
            return 0.0

        return temp

    @poissons_ratio.setter
    @enforce_parameter_types
    def poissons_ratio(self: Self, value: "float"):
        self.wrapped.PoissonsRatio = float(value) if value is not None else 0.0

    @property
    def shear_fatigue_strength(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearFatigueStrength

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_modulus(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearModulus

        if temp is None:
            return 0.0

        return temp

    @property
    def shear_yield_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShearYieldStress

        if temp is None:
            return 0.0

        return temp

    @property
    def specific_heat(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SpecificHeat

        if temp is None:
            return 0.0

        return temp

    @specific_heat.setter
    @enforce_parameter_types
    def specific_heat(self: Self, value: "float"):
        self.wrapped.SpecificHeat = float(value) if value is not None else 0.0

    @property
    def standard(self: Self) -> "_281.MaterialStandards":
        """mastapy.materials.MaterialStandards

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Standard

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.MaterialStandards"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials._281", "MaterialStandards"
        )(value)

    @property
    def surface_hardness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.SurfaceHardness

        if temp is None:
            return 0.0

        return temp

    @surface_hardness.setter
    @enforce_parameter_types
    def surface_hardness(self: Self, value: "float"):
        self.wrapped.SurfaceHardness = float(value) if value is not None else 0.0

    @property
    def surface_hardness_range_max_in_hb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hrc(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_max_in_hv(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMaxInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hb(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHB

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hrc(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHRC

        if temp is None:
            return 0.0

        return temp

    @property
    def surface_hardness_range_min_in_hv(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SurfaceHardnessRangeMinInHV

        if temp is None:
            return 0.0

        return temp

    @property
    def tensile_yield_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.TensileYieldStrength

        if temp is None:
            return 0.0

        return temp

    @tensile_yield_strength.setter
    @enforce_parameter_types
    def tensile_yield_strength(self: Self, value: "float"):
        self.wrapped.TensileYieldStrength = float(value) if value is not None else 0.0

    @property
    def ultimate_tensile_strength(self: Self) -> "float":
        """float"""
        temp = self.wrapped.UltimateTensileStrength

        if temp is None:
            return 0.0

        return temp

    @ultimate_tensile_strength.setter
    @enforce_parameter_types
    def ultimate_tensile_strength(self: Self, value: "float"):
        self.wrapped.UltimateTensileStrength = (
            float(value) if value is not None else 0.0
        )

    @property
    def cast_to(self: Self) -> "Material._Cast_Material":
        return self._Cast_Material(self)
