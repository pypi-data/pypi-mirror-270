"""RollerBearingProfile"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLER_BEARING_PROFILE = python_net_import(
    "SMT.MastaAPI.Bearings.RollerBearingProfiles", "RollerBearingProfile"
)

if TYPE_CHECKING:
    from mastapy.bearings.roller_bearing_profiles import (
        _1947,
        _1948,
        _1949,
        _1950,
        _1951,
        _1952,
        _1954,
        _1955,
    )


__docformat__ = "restructuredtext en"
__all__ = ("RollerBearingProfile",)


Self = TypeVar("Self", bound="RollerBearingProfile")


class RollerBearingProfile(_0.APIBase):
    """RollerBearingProfile

    This is a mastapy class.
    """

    TYPE = _ROLLER_BEARING_PROFILE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollerBearingProfile")

    class _Cast_RollerBearingProfile:
        """Special nested class for casting RollerBearingProfile to subclasses."""

        def __init__(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
            parent: "RollerBearingProfile",
        ):
            self._parent = parent

        @property
        def roller_bearing_conical_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1947.RollerBearingConicalProfile":
            from mastapy.bearings.roller_bearing_profiles import _1947

            return self._parent._cast(_1947.RollerBearingConicalProfile)

        @property
        def roller_bearing_crowned_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1948.RollerBearingCrownedProfile":
            from mastapy.bearings.roller_bearing_profiles import _1948

            return self._parent._cast(_1948.RollerBearingCrownedProfile)

        @property
        def roller_bearing_din_lundberg_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1949.RollerBearingDinLundbergProfile":
            from mastapy.bearings.roller_bearing_profiles import _1949

            return self._parent._cast(_1949.RollerBearingDinLundbergProfile)

        @property
        def roller_bearing_flat_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1950.RollerBearingFlatProfile":
            from mastapy.bearings.roller_bearing_profiles import _1950

            return self._parent._cast(_1950.RollerBearingFlatProfile)

        @property
        def roller_bearing_johns_gohar_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1951.RollerBearingJohnsGoharProfile":
            from mastapy.bearings.roller_bearing_profiles import _1951

            return self._parent._cast(_1951.RollerBearingJohnsGoharProfile)

        @property
        def roller_bearing_lundberg_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1952.RollerBearingLundbergProfile":
            from mastapy.bearings.roller_bearing_profiles import _1952

            return self._parent._cast(_1952.RollerBearingLundbergProfile)

        @property
        def roller_bearing_tangential_crowned_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1954.RollerBearingTangentialCrownedProfile":
            from mastapy.bearings.roller_bearing_profiles import _1954

            return self._parent._cast(_1954.RollerBearingTangentialCrownedProfile)

        @property
        def roller_bearing_user_specified_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "_1955.RollerBearingUserSpecifiedProfile":
            from mastapy.bearings.roller_bearing_profiles import _1955

            return self._parent._cast(_1955.RollerBearingUserSpecifiedProfile)

        @property
        def roller_bearing_profile(
            self: "RollerBearingProfile._Cast_RollerBearingProfile",
        ) -> "RollerBearingProfile":
            return self._parent

        def __getattr__(
            self: "RollerBearingProfile._Cast_RollerBearingProfile", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollerBearingProfile.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def covers_two_rows_of_elements(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.CoversTwoRowsOfElements

        if temp is None:
            return False

        return temp

    @covers_two_rows_of_elements.setter
    @enforce_parameter_types
    def covers_two_rows_of_elements(self: Self, value: "bool"):
        self.wrapped.CoversTwoRowsOfElements = (
            bool(value) if value is not None else False
        )

    @property
    def cast_to(self: Self) -> "RollerBearingProfile._Cast_RollerBearingProfile":
        return self._Cast_RollerBearingProfile(self)
