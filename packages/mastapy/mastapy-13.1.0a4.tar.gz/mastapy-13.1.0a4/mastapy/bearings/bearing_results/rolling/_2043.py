"""LoadedNonBarrelRollerBearingRow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _2048
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_ROW = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedNonBarrelRollerBearingRow"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _2042,
        _2013,
        _2016,
        _2028,
        _2040,
        _2067,
        _2052,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingRow",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingRow")


class LoadedNonBarrelRollerBearingRow(_2048.LoadedRollerBearingRow):
    """LoadedNonBarrelRollerBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_ROW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingRow")

    class _Cast_LoadedNonBarrelRollerBearingRow:
        """Special nested class for casting LoadedNonBarrelRollerBearingRow to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
            parent: "LoadedNonBarrelRollerBearingRow",
        ):
            self._parent = parent

        @property
        def loaded_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2048.LoadedRollerBearingRow":
            return self._parent._cast(_2048.LoadedRollerBearingRow)

        @property
        def loaded_rolling_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2052.LoadedRollingBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2052

            return self._parent._cast(_2052.LoadedRollingBearingRow)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2013.LoadedAxialThrustCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2013

            return self._parent._cast(
                _2013.LoadedAxialThrustCylindricalRollerBearingRow
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2016.LoadedAxialThrustNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2016

            return self._parent._cast(_2016.LoadedAxialThrustNeedleRollerBearingRow)

        @property
        def loaded_cylindrical_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2028.LoadedCylindricalRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2028

            return self._parent._cast(_2028.LoadedCylindricalRollerBearingRow)

        @property
        def loaded_needle_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2040.LoadedNeedleRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2040

            return self._parent._cast(_2040.LoadedNeedleRollerBearingRow)

        @property
        def loaded_taper_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "_2067.LoadedTaperRollerBearingRow":
            from mastapy.bearings.bearing_results.rolling import _2067

            return self._parent._cast(_2067.LoadedTaperRollerBearingRow)

        @property
        def loaded_non_barrel_roller_bearing_row(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
        ) -> "LoadedNonBarrelRollerBearingRow":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonBarrelRollerBearingRow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rib_normal_contact_stress_inner_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_inner_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressInnerRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_left(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterLeft

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def rib_normal_contact_stress_outer_right(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RibNormalContactStressOuterRight

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def loaded_bearing(self: Self) -> "_2042.LoadedNonBarrelRollerBearingResults":
        """mastapy.bearings.bearing_results.rolling.LoadedNonBarrelRollerBearingResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LoadedBearing

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonBarrelRollerBearingRow._Cast_LoadedNonBarrelRollerBearingRow":
        return self._Cast_LoadedNonBarrelRollerBearingRow(self)
