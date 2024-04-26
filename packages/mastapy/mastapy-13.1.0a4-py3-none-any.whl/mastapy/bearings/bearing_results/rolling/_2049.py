"""LoadedRollerStripLoadResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLER_STRIP_LOAD_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "LoadedRollerStripLoadResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import (
        _1999,
        _2009,
        _2044,
        _2060,
        _2077,
    )


__docformat__ = "restructuredtext en"
__all__ = ("LoadedRollerStripLoadResults",)


Self = TypeVar("Self", bound="LoadedRollerStripLoadResults")


class LoadedRollerStripLoadResults(_0.APIBase):
    """LoadedRollerStripLoadResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLER_STRIP_LOAD_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedRollerStripLoadResults")

    class _Cast_LoadedRollerStripLoadResults:
        """Special nested class for casting LoadedRollerStripLoadResults to subclasses."""

        def __init__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            parent: "LoadedRollerStripLoadResults",
        ):
            self._parent = parent

        @property
        def loaded_abstract_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_1999.LoadedAbstractSphericalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _1999

            return self._parent._cast(
                _1999.LoadedAbstractSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2009.LoadedAsymmetricSphericalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(
                _2009.LoadedAsymmetricSphericalRollerBearingStripLoadResults
            )

        @property
        def loaded_non_barrel_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2044.LoadedNonBarrelRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2044

            return self._parent._cast(
                _2044.LoadedNonBarrelRollerBearingStripLoadResults
            )

        @property
        def loaded_spherical_roller_radial_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2060.LoadedSphericalRollerRadialBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2060

            return self._parent._cast(
                _2060.LoadedSphericalRollerRadialBearingStripLoadResults
            )

        @property
        def loaded_toroidal_roller_bearing_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "_2077.LoadedToroidalRollerBearingStripLoadResults":
            from mastapy.bearings.bearing_results.rolling import _2077

            return self._parent._cast(_2077.LoadedToroidalRollerBearingStripLoadResults)

        @property
        def loaded_roller_strip_load_results(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
        ) -> "LoadedRollerStripLoadResults":
            return self._parent

        def __getattr__(
            self: "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedRollerStripLoadResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedRollerStripLoadResults._Cast_LoadedRollerStripLoadResults":
        return self._Cast_LoadedRollerStripLoadResults(self)
