"""GearMaterial"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.materials import _276
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MATERIAL = python_net_import("SMT.MastaAPI.Gears.Materials", "GearMaterial")

if TYPE_CHECKING:
    from mastapy.materials import _288
    from mastapy.gears.materials import _590, _592, _594, _598, _604, _608, _610
    from mastapy.utility.databases import _1844


__docformat__ = "restructuredtext en"
__all__ = ("GearMaterial",)


Self = TypeVar("Self", bound="GearMaterial")


class GearMaterial(_276.Material):
    """GearMaterial

    This is a mastapy class.
    """

    TYPE = _GEAR_MATERIAL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMaterial")

    class _Cast_GearMaterial:
        """Special nested class for casting GearMaterial to subclasses."""

        def __init__(self: "GearMaterial._Cast_GearMaterial", parent: "GearMaterial"):
            self._parent = parent

        @property
        def material(self: "GearMaterial._Cast_GearMaterial") -> "_276.Material":
            return self._parent._cast(_276.Material)

        @property
        def named_database_item(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_1844.NamedDatabaseItem":
            from mastapy.utility.databases import _1844

            return self._parent._cast(_1844.NamedDatabaseItem)

        @property
        def agma_cylindrical_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_590.AGMACylindricalGearMaterial":
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.AGMACylindricalGearMaterial)

        @property
        def bevel_gear_iso_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_592.BevelGearISOMaterial":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.BevelGearISOMaterial)

        @property
        def bevel_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_594.BevelGearMaterial":
            from mastapy.gears.materials import _594

            return self._parent._cast(_594.BevelGearMaterial)

        @property
        def cylindrical_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_598.CylindricalGearMaterial":
            from mastapy.gears.materials import _598

            return self._parent._cast(_598.CylindricalGearMaterial)

        @property
        def iso_cylindrical_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_604.ISOCylindricalGearMaterial":
            from mastapy.gears.materials import _604

            return self._parent._cast(_604.ISOCylindricalGearMaterial)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_608.KlingelnbergCycloPalloidConicalGearMaterial":
            from mastapy.gears.materials import _608

            return self._parent._cast(_608.KlingelnbergCycloPalloidConicalGearMaterial)

        @property
        def plastic_cylindrical_gear_material(
            self: "GearMaterial._Cast_GearMaterial",
        ) -> "_610.PlasticCylindricalGearMaterial":
            from mastapy.gears.materials import _610

            return self._parent._cast(_610.PlasticCylindricalGearMaterial)

        @property
        def gear_material(self: "GearMaterial._Cast_GearMaterial") -> "GearMaterial":
            return self._parent

        def __getattr__(self: "GearMaterial._Cast_GearMaterial", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMaterial.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def apply_derating_factors_to_bending_custom_sn_curve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyDeratingFactorsToBendingCustomSNCurve

        if temp is None:
            return False

        return temp

    @apply_derating_factors_to_bending_custom_sn_curve.setter
    @enforce_parameter_types
    def apply_derating_factors_to_bending_custom_sn_curve(self: Self, value: "bool"):
        self.wrapped.ApplyDeratingFactorsToBendingCustomSNCurve = (
            bool(value) if value is not None else False
        )

    @property
    def apply_derating_factors_to_contact_custom_sn_curve(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ApplyDeratingFactorsToContactCustomSNCurve

        if temp is None:
            return False

        return temp

    @apply_derating_factors_to_contact_custom_sn_curve.setter
    @enforce_parameter_types
    def apply_derating_factors_to_contact_custom_sn_curve(self: Self, value: "bool"):
        self.wrapped.ApplyDeratingFactorsToContactCustomSNCurve = (
            bool(value) if value is not None else False
        )

    @property
    def core_hardness(self: Self) -> "float":
        """float"""
        temp = self.wrapped.CoreHardness

        if temp is None:
            return 0.0

        return temp

    @core_hardness.setter
    @enforce_parameter_types
    def core_hardness(self: Self, value: "float"):
        self.wrapped.CoreHardness = float(value) if value is not None else 0.0

    @property
    def n0_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Bending

        if temp is None:
            return 0.0

        return temp

    @property
    def n0_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.N0Contact

        if temp is None:
            return 0.0

        return temp

    @property
    def nc_bending(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NCBending

        if temp is None:
            return 0.0

        return temp

    @property
    def nc_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NCContact

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_known_points_for_user_sn_curve_bending_stress(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfKnownPointsForUserSNCurveBendingStress

        if temp is None:
            return 0

        return temp

    @property
    def number_of_known_points_for_user_sn_curve_for_contact_stress(
        self: Self,
    ) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfKnownPointsForUserSNCurveForContactStress

        if temp is None:
            return 0

        return temp

    @property
    def sn_curve_bending(self: Self) -> "_288.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveBending

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def sn_curve_contact(self: Self) -> "_288.SNCurve":
        """mastapy.materials.SNCurve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SNCurveContact

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMaterial._Cast_GearMaterial":
        return self._Cast_GearMaterial(self)
