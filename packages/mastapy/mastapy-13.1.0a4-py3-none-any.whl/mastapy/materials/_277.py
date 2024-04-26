"""MaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1843
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MATERIAL_DATABASE = python_net_import("SMT.MastaAPI.Materials", "MaterialDatabase")

if TYPE_CHECKING:
    from mastapy.materials import _276
    from mastapy.shafts import _25
    from mastapy.gears.materials import _591, _593, _596, _597, _599, _600
    from mastapy.electric_machines import _1296, _1314, _1327
    from mastapy.cycloidal import _1469, _1476
    from mastapy.utility.databases import _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("MaterialDatabase",)


Self = TypeVar("Self", bound="MaterialDatabase")
T = TypeVar("T", bound="_276.Material")


class MaterialDatabase(_1843.NamedDatabase[T]):
    """MaterialDatabase

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MaterialDatabase")

    class _Cast_MaterialDatabase:
        """Special nested class for casting MaterialDatabase to subclasses."""

        def __init__(
            self: "MaterialDatabase._Cast_MaterialDatabase", parent: "MaterialDatabase"
        ):
            self._parent = parent

        @property
        def named_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1843.NamedDatabase":
            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def shaft_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_591.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _591

            return self._parent._cast(_591.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_593.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.BevelGearISOMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_596.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_597.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _597

            return self._parent._cast(_597.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_599.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _599

            return self._parent._cast(_599.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_600.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.CylindricalGearPlasticMaterialDatabase)

        @property
        def magnet_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1296.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1296

            return self._parent._cast(_1296.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1314.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1314

            return self._parent._cast(_1314.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1327.WindingMaterialDatabase":
            from mastapy.electric_machines import _1327

            return self._parent._cast(_1327.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1469.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1469

            return self._parent._cast(_1469.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "_1476.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1476

            return self._parent._cast(_1476.RingPinsMaterialDatabase)

        @property
        def material_database(
            self: "MaterialDatabase._Cast_MaterialDatabase",
        ) -> "MaterialDatabase":
            return self._parent

        def __getattr__(self: "MaterialDatabase._Cast_MaterialDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MaterialDatabase._Cast_MaterialDatabase":
        return self._Cast_MaterialDatabase(self)
