"""GBT3478SplineHalfDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.detailed_rigid_connectors.splines import _1411
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GBT3478_SPLINE_HALF_DESIGN = python_net_import(
    "SMT.MastaAPI.DetailedRigidConnectors.Splines", "GBT3478SplineHalfDesign"
)

if TYPE_CHECKING:
    from mastapy.detailed_rigid_connectors.splines import _1431, _1426
    from mastapy.detailed_rigid_connectors import _1400


__docformat__ = "restructuredtext en"
__all__ = ("GBT3478SplineHalfDesign",)


Self = TypeVar("Self", bound="GBT3478SplineHalfDesign")


class GBT3478SplineHalfDesign(_1411.ISO4156SplineHalfDesign):
    """GBT3478SplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _GBT3478_SPLINE_HALF_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GBT3478SplineHalfDesign")

    class _Cast_GBT3478SplineHalfDesign:
        """Special nested class for casting GBT3478SplineHalfDesign to subclasses."""

        def __init__(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
            parent: "GBT3478SplineHalfDesign",
        ):
            self._parent = parent

        @property
        def iso4156_spline_half_design(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
        ) -> "_1411.ISO4156SplineHalfDesign":
            return self._parent._cast(_1411.ISO4156SplineHalfDesign)

        @property
        def standard_spline_half_design(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
        ) -> "_1431.StandardSplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1431

            return self._parent._cast(_1431.StandardSplineHalfDesign)

        @property
        def spline_half_design(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
        ) -> "_1426.SplineHalfDesign":
            from mastapy.detailed_rigid_connectors.splines import _1426

            return self._parent._cast(_1426.SplineHalfDesign)

        @property
        def detailed_rigid_connector_half_design(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
        ) -> "_1400.DetailedRigidConnectorHalfDesign":
            from mastapy.detailed_rigid_connectors import _1400

            return self._parent._cast(_1400.DetailedRigidConnectorHalfDesign)

        @property
        def gbt3478_spline_half_design(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign",
        ) -> "GBT3478SplineHalfDesign":
            return self._parent

        def __getattr__(
            self: "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GBT3478SplineHalfDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GBT3478SplineHalfDesign._Cast_GBT3478SplineHalfDesign":
        return self._Cast_GBT3478SplineHalfDesign(self)
