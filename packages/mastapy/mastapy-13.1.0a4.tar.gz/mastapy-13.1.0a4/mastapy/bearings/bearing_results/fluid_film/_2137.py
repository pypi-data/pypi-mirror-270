"""LoadedFluidFilmBearingResults"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_FLUID_FILM_BEARING_RESULTS = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.FluidFilm", "LoadedFluidFilmBearingResults"
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.fluid_film import (
        _2138,
        _2139,
        _2140,
        _2142,
        _2145,
        _2146,
    )
    from mastapy.bearings.bearing_results import _1975, _1967
    from mastapy.bearings import _1892


__docformat__ = "restructuredtext en"
__all__ = ("LoadedFluidFilmBearingResults",)


Self = TypeVar("Self", bound="LoadedFluidFilmBearingResults")


class LoadedFluidFilmBearingResults(_1972.LoadedDetailedBearingResults):
    """LoadedFluidFilmBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_FLUID_FILM_BEARING_RESULTS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_LoadedFluidFilmBearingResults")

    class _Cast_LoadedFluidFilmBearingResults:
        """Special nested class for casting LoadedFluidFilmBearingResults to subclasses."""

        def __init__(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
            parent: "LoadedFluidFilmBearingResults",
        ):
            self._parent = parent

        @property
        def loaded_detailed_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1972.LoadedDetailedBearingResults":
            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_1892.BearingLoadCaseResultsLightweight":
            from mastapy.bearings import _1892

            return self._parent._cast(_1892.BearingLoadCaseResultsLightweight)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2138.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2138

            return self._parent._cast(_2138.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2139.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2140.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2142.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2145.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2145

            return self._parent._cast(_2145.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "_2146.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2146

            return self._parent._cast(_2146.LoadedTiltingPadThrustBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
        ) -> "LoadedFluidFilmBearingResults":
            return self._parent

        def __getattr__(
            self: "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "LoadedFluidFilmBearingResults.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def relative_misalignment(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RelativeMisalignment

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedFluidFilmBearingResults._Cast_LoadedFluidFilmBearingResults":
        return self._Cast_LoadedFluidFilmBearingResults(self)
