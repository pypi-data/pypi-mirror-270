"""MultiPointContactBallBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2158
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MULTI_POINT_CONTACT_BALL_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "MultiPointContactBallBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2172, _2190, _2183
    from mastapy.bearings.bearing_designs import _2149, _2152, _2148


__docformat__ = "restructuredtext en"
__all__ = ("MultiPointContactBallBearing",)


Self = TypeVar("Self", bound="MultiPointContactBallBearing")


class MultiPointContactBallBearing(_2158.BallBearing):
    """MultiPointContactBallBearing

    This is a mastapy class.
    """

    TYPE = _MULTI_POINT_CONTACT_BALL_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MultiPointContactBallBearing")

    class _Cast_MultiPointContactBallBearing:
        """Special nested class for casting MultiPointContactBallBearing to subclasses."""

        def __init__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            parent: "MultiPointContactBallBearing",
        ):
            self._parent = parent

        @property
        def ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2158.BallBearing":
            return self._parent._cast(_2158.BallBearing)

        @property
        def rolling_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2183.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2183

            return self._parent._cast(_2183.RollingBearing)

        @property
        def detailed_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2149.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2149

            return self._parent._cast(_2149.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2152.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2152

            return self._parent._cast(_2152.NonLinearBearing)

        @property
        def bearing_design(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2148.BearingDesign":
            from mastapy.bearings.bearing_designs import _2148

            return self._parent._cast(_2148.BearingDesign)

        @property
        def four_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2172.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.FourPointContactBallBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "_2190.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2190

            return self._parent._cast(_2190.ThreePointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
        ) -> "MultiPointContactBallBearing":
            return self._parent

        def __getattr__(
            self: "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MultiPointContactBallBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MultiPointContactBallBearing._Cast_MultiPointContactBallBearing":
        return self._Cast_MultiPointContactBallBearing(self)
