"""DetailedBearing"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_designs import _2152
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DETAILED_BEARING = python_net_import(
    "SMT.MastaAPI.Bearings.BearingDesigns", "DetailedBearing"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_designs.rolling import (
        _2153,
        _2154,
        _2155,
        _2156,
        _2157,
        _2158,
        _2160,
        _2166,
        _2167,
        _2168,
        _2172,
        _2177,
        _2178,
        _2179,
        _2180,
        _2183,
        _2184,
        _2187,
        _2188,
        _2189,
        _2190,
        _2191,
        _2192,
    )
    from mastapy.bearings.bearing_designs.fluid_film import (
        _2205,
        _2207,
        _2209,
        _2211,
        _2212,
        _2213,
    )
    from mastapy.bearings.bearing_designs import _2148


__docformat__ = "restructuredtext en"
__all__ = ("DetailedBearing",)


Self = TypeVar("Self", bound="DetailedBearing")


class DetailedBearing(_2152.NonLinearBearing):
    """DetailedBearing

    This is a mastapy class.
    """

    TYPE = _DETAILED_BEARING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DetailedBearing")

    class _Cast_DetailedBearing:
        """Special nested class for casting DetailedBearing to subclasses."""

        def __init__(
            self: "DetailedBearing._Cast_DetailedBearing", parent: "DetailedBearing"
        ):
            self._parent = parent

        @property
        def non_linear_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2152.NonLinearBearing":
            return self._parent._cast(_2152.NonLinearBearing)

        @property
        def bearing_design(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2148.BearingDesign":
            from mastapy.bearings.bearing_designs import _2148

            return self._parent._cast(_2148.BearingDesign)

        @property
        def angular_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2153.AngularContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2153

            return self._parent._cast(_2153.AngularContactBallBearing)

        @property
        def angular_contact_thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2154.AngularContactThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2154

            return self._parent._cast(_2154.AngularContactThrustBallBearing)

        @property
        def asymmetric_spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2155.AsymmetricSphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2155

            return self._parent._cast(_2155.AsymmetricSphericalRollerBearing)

        @property
        def axial_thrust_cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2156.AxialThrustCylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2156

            return self._parent._cast(_2156.AxialThrustCylindricalRollerBearing)

        @property
        def axial_thrust_needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2157.AxialThrustNeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2157

            return self._parent._cast(_2157.AxialThrustNeedleRollerBearing)

        @property
        def ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2158.BallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2158

            return self._parent._cast(_2158.BallBearing)

        @property
        def barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2160.BarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2160

            return self._parent._cast(_2160.BarrelRollerBearing)

        @property
        def crossed_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2166.CrossedRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2166

            return self._parent._cast(_2166.CrossedRollerBearing)

        @property
        def cylindrical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2167.CylindricalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2167

            return self._parent._cast(_2167.CylindricalRollerBearing)

        @property
        def deep_groove_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2168.DeepGrooveBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2168

            return self._parent._cast(_2168.DeepGrooveBallBearing)

        @property
        def four_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2172.FourPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2172

            return self._parent._cast(_2172.FourPointContactBallBearing)

        @property
        def multi_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2177.MultiPointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2177

            return self._parent._cast(_2177.MultiPointContactBallBearing)

        @property
        def needle_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2178.NeedleRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2178

            return self._parent._cast(_2178.NeedleRollerBearing)

        @property
        def non_barrel_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2179.NonBarrelRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2179

            return self._parent._cast(_2179.NonBarrelRollerBearing)

        @property
        def roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2180.RollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2180

            return self._parent._cast(_2180.RollerBearing)

        @property
        def rolling_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2183.RollingBearing":
            from mastapy.bearings.bearing_designs.rolling import _2183

            return self._parent._cast(_2183.RollingBearing)

        @property
        def self_aligning_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2184.SelfAligningBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2184

            return self._parent._cast(_2184.SelfAligningBallBearing)

        @property
        def spherical_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2187.SphericalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2187

            return self._parent._cast(_2187.SphericalRollerBearing)

        @property
        def spherical_roller_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2188.SphericalRollerThrustBearing":
            from mastapy.bearings.bearing_designs.rolling import _2188

            return self._parent._cast(_2188.SphericalRollerThrustBearing)

        @property
        def taper_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2189.TaperRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2189

            return self._parent._cast(_2189.TaperRollerBearing)

        @property
        def three_point_contact_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2190.ThreePointContactBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2190

            return self._parent._cast(_2190.ThreePointContactBallBearing)

        @property
        def thrust_ball_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2191.ThrustBallBearing":
            from mastapy.bearings.bearing_designs.rolling import _2191

            return self._parent._cast(_2191.ThrustBallBearing)

        @property
        def toroidal_roller_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2192.ToroidalRollerBearing":
            from mastapy.bearings.bearing_designs.rolling import _2192

            return self._parent._cast(_2192.ToroidalRollerBearing)

        @property
        def pad_fluid_film_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2205.PadFluidFilmBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2205

            return self._parent._cast(_2205.PadFluidFilmBearing)

        @property
        def plain_grease_filled_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2207.PlainGreaseFilledJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2207

            return self._parent._cast(_2207.PlainGreaseFilledJournalBearing)

        @property
        def plain_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2209.PlainJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2209

            return self._parent._cast(_2209.PlainJournalBearing)

        @property
        def plain_oil_fed_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2211.PlainOilFedJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2211

            return self._parent._cast(_2211.PlainOilFedJournalBearing)

        @property
        def tilting_pad_journal_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2212.TiltingPadJournalBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2212

            return self._parent._cast(_2212.TiltingPadJournalBearing)

        @property
        def tilting_pad_thrust_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "_2213.TiltingPadThrustBearing":
            from mastapy.bearings.bearing_designs.fluid_film import _2213

            return self._parent._cast(_2213.TiltingPadThrustBearing)

        @property
        def detailed_bearing(
            self: "DetailedBearing._Cast_DetailedBearing",
        ) -> "DetailedBearing":
            return self._parent

        def __getattr__(self: "DetailedBearing._Cast_DetailedBearing", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DetailedBearing.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DetailedBearing._Cast_DetailedBearing":
        return self._Cast_DetailedBearing(self)
