"""CrossedRollerBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs.rolling import _2180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CROSSED_ROLLER_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns.Rolling", "CrossedRollerBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import _2183
    from mastapy.bearings.bearing_designs import _2149, _2152, _2148


__docformat__ = "restructuredtext en"
__all__ = ("CrossedRollerBearing",)


Self = TypeVar("Self", bound="CrossedRollerBearing")


class CrossedRollerBearing(_2180.RollerBearing):
    """CrossedRollerBearing

    This is a mastapy class.
    """

    TYPE = _CROSSED_ROLLER_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CrossedRollerBearing")

    class _Cast_CrossedRollerBearing:
        """Special nested class for casting CrossedRollerBearing to subclasses."""

        def __init__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
            parent: "CrossedRollerBearing",
        ):
            self._parent = parent

        @property
        def roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2180.RollerBearing":
            return self._parent._cast(_2180.RollerBearing)

        @property
        def rolling_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2183.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2183

            return self._parent._cast(_2183.RollingBearing)

        @property
        def detailed_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2149.DetailedBearing":
            from mastapy.bearings.bearing_designs import _2149

            return self._parent._cast(_2149.DetailedBearing)

        @property
        def non_linear_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2152.NonLinearBearing":
            from mastapy.bearings.bearing_designs import _2152

            return self._parent._cast(_2152.NonLinearBearing)

        @property
        def bearing_design(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "_2148.BearingDesign":
            from mastapy.bearings.bearing_designs import _2148

            return self._parent._cast(_2148.BearingDesign)

        @property
        def crossed_roller_bearing(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing",
        ) -> "CrossedRollerBearing":
            return self._parent

        def __getattr__(
            self: "CrossedRollerBearing._Cast_CrossedRollerBearing", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CrossedRollerBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "CrossedRollerBearing._Cast_CrossedRollerBearing":
        return self._Cast_CrossedRollerBearing(self)
