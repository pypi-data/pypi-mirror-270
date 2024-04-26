"""SplineJointRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy.detailed_rigid_connectors.rating import _1448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_JOINT_RATING = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings", "SplineJointRating"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines.ratings import (
        _1443,
        _1436,
        _1438,
        _1440,
        _1442,
    )


__docformat__ = "restructuredtext en"
__all__ = ("SplineJointRating",)


Self = TypeVar("Self", bound="SplineJointRating")


class SplineJointRating(_1448.ShaftHubConnectionRating):
    """SplineJointRating

    This is a mastapy class.
    """

    TYPE = _SPLINE_JOINT_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineJointRating")

    class _Cast_SplineJointRating:
        """Special nested class for casting SplineJointRating to subclasses."""

        def __init__(
            self: "SplineJointRating._Cast_SplineJointRating",
            parent: "SplineJointRating",
        ):
            self._parent = parent

        @property
        def shaft_hub_connection_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "_1448.ShaftHubConnectionRating":
            return self._parent._cast(_1448.ShaftHubConnectionRating)

        @property
        def agma6123_spline_joint_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "_1436.AGMA6123SplineJointRating":
            from mastapy.detailed_rigid_connectors.splines.ratings import _1436

            return self._parent._cast(_1436.AGMA6123SplineJointRating)

        @property
        def din5466_spline_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "_1438.DIN5466SplineRating":
            from mastapy.detailed_rigid_connectors.splines.ratings import _1438

            return self._parent._cast(_1438.DIN5466SplineRating)

        @property
        def gbt17855_spline_joint_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "_1440.GBT17855SplineJointRating":
            from mastapy.detailed_rigid_connectors.splines.ratings import _1440

            return self._parent._cast(_1440.GBT17855SplineJointRating)

        @property
        def sae_spline_joint_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "_1442.SAESplineJointRating":
            from mastapy.detailed_rigid_connectors.splines.ratings import _1442

            return self._parent._cast(_1442.SAESplineJointRating)

        @property
        def spline_joint_rating(
            self: "SplineJointRating._Cast_SplineJointRating",
        ) -> "SplineJointRating":
            return self._parent

        def __getattr__(self: "SplineJointRating._Cast_SplineJointRating", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineJointRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBendingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_bursting_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableBurstingStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_compressive_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableCompressiveStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_contact_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableContactStress

        if temp is None:
            return 0.0

        return temp

    @property
    def allowable_shear_stress(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowableShearStress

        if temp is None:
            return 0.0

        return temp

    @property
    def dudley_maximum_effective_length(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DudleyMaximumEffectiveLength

        if temp is None:
            return 0.0

        return temp

    @property
    def load(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Load

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_cycles(self: Self) -> "float":
        """float"""
        temp = self.wrapped.NumberOfCycles

        if temp is None:
            return 0.0

        return temp

    @number_of_cycles.setter
    @enforce_parameter_types
    def number_of_cycles(self: Self, value: "float"):
        self.wrapped.NumberOfCycles = float(value) if value is not None else 0.0

    @property
    def spline_half_ratings(self: Self) -> "List[_1443.SplineHalfRating]":
        """List[mastapy.detailed_rigid_connectors.splines.ratings.SplineHalfRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SplineHalfRatings

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "SplineJointRating._Cast_SplineJointRating":
        return self._Cast_SplineJointRating(self)
