"""AxialThrustCylindricalRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2179
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling",
    "AxialThrustCylindricalRollerBearing",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2157, _2180, _2183
    from mastapy.bearings.bearing_designs import _2149, _2152, _2148


__docformat__ = "restructuredtext en"
__all__ = ("AxialThrustCylindricalRollerBearing",)


Self = TypeVar("Self", bound="AxialThrustCylindricalRollerBearing")


class AxialThrustCylindricalRollerBearing(_2179.NonBarrelRollerBearing):
    """AxialThrustCylindricalRollerBearing

    This is a mastapy class.
    """

    TYPE = _AXIAL_THRUST_CYLINDRICAL_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AxialThrustCylindricalRollerBearing")

    class _Cast_AxialThrustCylindricalRollerBearing:
        """Special nested class for casting AxialThrustCylindricalRollerBearing to subclasses."""

        def __init__(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
            parent: "AxialThrustCylindricalRollerBearing",
        ):
            self._parent = parent

        @property
        def non_barrel_roller_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2179.NonBarrelRollerBearing":
            return self._parent._cast(_2179.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2180.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.RollerBearing)

        @property
        def rolling_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2183.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2183

            return self._parent._cast(_2183.RollingBearing)

        @property
        def detailed_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2149.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2149

            return self._parent._cast(_2149.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2152.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2152

            return self._parent._cast(_2152.NonLinearBearing)

        @property
        def bearing_design(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2148.BearingDesign":
            from mastapy.bearings.bearing_designs import _2148

            return self._parent._cast(_2148.BearingDesign)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "_2157.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.AxialThrustNeedleRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
        ) -> "AxialThrustCylindricalRollerBearing":
            return self._parent

        def __getattr__(
            self: "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing",
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
        self: Self, instance_to_wrap: "AxialThrustCylindricalRollerBearing.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AxialThrustCylindricalRollerBearing._Cast_AxialThrustCylindricalRollerBearing"
    ):
        return self._Cast_AxialThrustCylindricalRollerBearing(self)
