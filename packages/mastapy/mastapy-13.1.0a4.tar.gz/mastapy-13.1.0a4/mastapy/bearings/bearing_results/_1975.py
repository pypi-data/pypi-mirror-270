"""LoadedNonLinearBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.bearings.bearing_results import _1967
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_LINEAR_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults", "LoadedNonLinearBearingResults"
)

if TYPE_CHECKING:
    from mastapy.materials.efficiency import _309, _310
    from mastapy.bearings.bearing_results import _1969, _1970, _1971, _1972
    from mastapy.bearings.bearing_results.rolling import (
        _2001,
        _2004,
        _2007,
        _2012,
        _2015,
        _2020,
        _2023,
        _2027,
        _2030,
        _2035,
        _2039,
        _2042,
        _2047,
        _2051,
        _2054,
        _2058,
        _2061,
        _2066,
        _2069,
        _2072,
        _2075,
    )
    from mastapy.bearings.bearing_results.fluid_film import (
        _2137,
        _2138,
        _2139,
        _2140,
        _2142,
        _2145,
        _2146,
    )
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonLinearBearingResults",)


Self = TypeVar("Self", bound="LoadedNonLinearBearingResults")


class LoadedNonLinearBearingResults(_1967.LoadedBearingResults):
    """LoadedNonLinearBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_LINEAR_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedNonLinearBearingResults")

    class _Cast_LoadedNonLinearBearingResults:
        """Special nested class for casting LoadedNonLinearBearingResults to subclasses."""

        def __init__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            parent: "LoadedNonLinearBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1967.LoadedBearingResults":
            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1969.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1970.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1971.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1971

            return self._parent._cast(_1971.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2001.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(_2001.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2004.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(
                _2004.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2007.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(
                _2007.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2020.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2023.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2027.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2030.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2035.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2039.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2042.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2047.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2054.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2058.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2061.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2066.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2069.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2069

            return self._parent._cast(_2069.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2072.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2075.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2137.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2137

            return self._parent._cast(_2137.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2138.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2138

            return self._parent._cast(_2138.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2139.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2140.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2142.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2145.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2145

            return self._parent._cast(_2145.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "_2146.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2146

            return self._parent._cast(_2146.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
        ) -> "LoadedNonLinearBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedNonLinearBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def power_loss(self: Self) -> "_309.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_310.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonLinearBearingResults._Cast_LoadedNonLinearBearingResults":
        return self._Cast_LoadedNonLinearBearingResults(self)
