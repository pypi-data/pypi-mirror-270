"""CylindricalGearPlungeShaver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _722
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearPlungeShaver",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _620
    from mastapy.gears.manufacturing.cylindrical.cutters import _725, _720, _713
    from mastapy.utility.databases import _1844


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPlungeShaver",)


Self = TypeVar("Self", bound="CylindricalGearPlungeShaver")


class CylindricalGearPlungeShaver(_722.CylindricalGearShaver):
    """CylindricalGearPlungeShaver

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPlungeShaver")

    class _Cast_CylindricalGearPlungeShaver:
        """Special nested class for casting CylindricalGearPlungeShaver to subclasses."""

        def __init__(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
            parent: "CylindricalGearPlungeShaver",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_shaver(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "_722.CylindricalGearShaver":
            return self._parent._cast(_722.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "_725.InvoluteCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _725

            return self._parent._cast(_725.InvoluteCutterDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "_720.CylindricalGearRealCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "_713.CylindricalGearAbstractCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _713

            return self._parent._cast(_713.CylindricalGearAbstractCutterDesign)

        @property
        def named_database_item(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "_1844.NamedDatabaseItem":
            from mastapy.utility.databases import _1844

            return self._parent._cast(_1844.NamedDatabaseItem)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
        ) -> "CylindricalGearPlungeShaver":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearPlungeShaver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def has_tolerances(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.HasTolerances

        if temp is None:
            return False

        return temp

    @has_tolerances.setter
    @enforce_parameter_types
    def has_tolerances(self: Self, value: "bool"):
        self.wrapped.HasTolerances = bool(value) if value is not None else False

    @property
    def left_flank_micro_geometry(
        self: Self,
    ) -> "_620.CylindricalGearSpecifiedMicroGeometry":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LeftFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def right_flank_micro_geometry(
        self: Self,
    ) -> "_620.CylindricalGearSpecifiedMicroGeometry":
        """mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RightFlankMicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry(
        self: Self,
    ) -> "List[_620.CylindricalGearSpecifiedMicroGeometry]":
        """List[mastapy.gears.manufacturing.cylindrical.CylindricalGearSpecifiedMicroGeometry]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearPlungeShaver._Cast_CylindricalGearPlungeShaver":
        return self._Cast_CylindricalGearPlungeShaver(self)
