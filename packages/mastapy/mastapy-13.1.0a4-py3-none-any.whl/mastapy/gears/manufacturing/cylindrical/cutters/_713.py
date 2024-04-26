"""CylindricalGearAbstractCutterDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1844
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearAbstractCutterDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.cutters import (
        _714,
        _715,
        _716,
        _717,
        _719,
        _720,
        _721,
        _722,
        _725,
    )


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAbstractCutterDesign",)


Self = TypeVar("Self", bound="CylindricalGearAbstractCutterDesign")


class CylindricalGearAbstractCutterDesign(_1844.NamedDatabaseItem):
    """CylindricalGearAbstractCutterDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ABSTRACT_CUTTER_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearAbstractCutterDesign")

    class _Cast_CylindricalGearAbstractCutterDesign:
        """Special nested class for casting CylindricalGearAbstractCutterDesign to subclasses."""

        def __init__(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
            parent: "CylindricalGearAbstractCutterDesign",
        ):
            self._parent = parent

        @property
        def named_database_item(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_1844.NamedDatabaseItem":
            return self._parent._cast(_1844.NamedDatabaseItem)

        @property
        def cylindrical_gear_form_grinding_wheel(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_714.CylindricalGearFormGrindingWheel":
            from mastapy.gears.manufacturing.cylindrical.cutters import _714

            return self._parent._cast(_714.CylindricalGearFormGrindingWheel)

        @property
        def cylindrical_gear_grinding_worm(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_715.CylindricalGearGrindingWorm":
            from mastapy.gears.manufacturing.cylindrical.cutters import _715

            return self._parent._cast(_715.CylindricalGearGrindingWorm)

        @property
        def cylindrical_gear_hob_design(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_716.CylindricalGearHobDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearHobDesign)

        @property
        def cylindrical_gear_plunge_shaver(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_717.CylindricalGearPlungeShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalGearPlungeShaver)

        @property
        def cylindrical_gear_rack_design(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_719.CylindricalGearRackDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _719

            return self._parent._cast(_719.CylindricalGearRackDesign)

        @property
        def cylindrical_gear_real_cutter_design(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_720.CylindricalGearRealCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _720

            return self._parent._cast(_720.CylindricalGearRealCutterDesign)

        @property
        def cylindrical_gear_shaper(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_721.CylindricalGearShaper":
            from mastapy.gears.manufacturing.cylindrical.cutters import _721

            return self._parent._cast(_721.CylindricalGearShaper)

        @property
        def cylindrical_gear_shaver(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_722.CylindricalGearShaver":
            from mastapy.gears.manufacturing.cylindrical.cutters import _722

            return self._parent._cast(_722.CylindricalGearShaver)

        @property
        def involute_cutter_design(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "_725.InvoluteCutterDesign":
            from mastapy.gears.manufacturing.cylindrical.cutters import _725

            return self._parent._cast(_725.InvoluteCutterDesign)

        @property
        def cylindrical_gear_abstract_cutter_design(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
        ) -> "CylindricalGearAbstractCutterDesign":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign",
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
        self: Self, instance_to_wrap: "CylindricalGearAbstractCutterDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterType

        if temp is None:
            return ""

        return temp

    @property
    def edge_radius(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EdgeRadius

        if temp is None:
            return 0.0

        return temp

    @edge_radius.setter
    @enforce_parameter_types
    def edge_radius(self: Self, value: "float"):
        self.wrapped.EdgeRadius = float(value) if value is not None else 0.0

    @property
    def nominal_normal_pressure_angle(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.NominalNormalPressureAngle

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @nominal_normal_pressure_angle.setter
    @enforce_parameter_types
    def nominal_normal_pressure_angle(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.NominalNormalPressureAngle = value

    @property
    def normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalModule

        if temp is None:
            return 0.0

        return temp

    @normal_module.setter
    @enforce_parameter_types
    def normal_module(self: Self, value: "float"):
        self.wrapped.NormalModule = float(value) if value is not None else 0.0

    @property
    def normal_pressure_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NormalPressureAngle

        if temp is None:
            return 0.0

        return temp

    @normal_pressure_angle.setter
    @enforce_parameter_types
    def normal_pressure_angle(self: Self, value: "float"):
        self.wrapped.NormalPressureAngle = float(value) if value is not None else 0.0

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearAbstractCutterDesign._Cast_CylindricalGearAbstractCutterDesign"
    ):
        return self._Cast_CylindricalGearAbstractCutterDesign(self)
