"""BearingLoadCaseResultsLightweight"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT = python_net_import(
    "SMT.MastaAPI.Bearings", "BearingLoadCaseResultsLightweight"
)

if TYPE_CHECKING:
    from mastapy.bearings import _1891
    from mastapy.bearings.bearing_results import (
        _1967,
        _1969,
        _1970,
        _1971,
        _1972,
        _1973,
        _1975,
    )
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


__docformat__ = "restructuredtext en"
__all__ = ("BearingLoadCaseResultsLightweight",)


Self = TypeVar("Self", bound="BearingLoadCaseResultsLightweight")


class BearingLoadCaseResultsLightweight(_0.APIBase):
    """BearingLoadCaseResultsLightweight

    This is a mastapy class.
    """

    TYPE = _BEARING_LOAD_CASE_RESULTS_LIGHTWEIGHT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BearingLoadCaseResultsLightweight")

    class _Cast_BearingLoadCaseResultsLightweight:
        """Special nested class for casting BearingLoadCaseResultsLightweight to subclasses."""

        def __init__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            parent: "BearingLoadCaseResultsLightweight",
        ):
            self._parent = parent

        @property
        def bearing_load_case_results_for_pst(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1891.BearingLoadCaseResultsForPST":
            from mastapy.bearings import _1891

            return self._parent._cast(_1891.BearingLoadCaseResultsForPST)

        @property
        def loaded_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1967.LoadedBearingResults":
            from mastapy.bearings.bearing_results import _1967

            return self._parent._cast(_1967.LoadedBearingResults)

        @property
        def loaded_concept_axial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1969.LoadedConceptAxialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1969

            return self._parent._cast(_1969.LoadedConceptAxialClearanceBearingResults)

        @property
        def loaded_concept_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1970.LoadedConceptClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1970

            return self._parent._cast(_1970.LoadedConceptClearanceBearingResults)

        @property
        def loaded_concept_radial_clearance_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1971.LoadedConceptRadialClearanceBearingResults":
            from mastapy.bearings.bearing_results import _1971

            return self._parent._cast(_1971.LoadedConceptRadialClearanceBearingResults)

        @property
        def loaded_detailed_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1972.LoadedDetailedBearingResults":
            from mastapy.bearings.bearing_results import _1972

            return self._parent._cast(_1972.LoadedDetailedBearingResults)

        @property
        def loaded_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1973.LoadedLinearBearingResults":
            from mastapy.bearings.bearing_results import _1973

            return self._parent._cast(_1973.LoadedLinearBearingResults)

        @property
        def loaded_non_linear_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_1975.LoadedNonLinearBearingResults":
            from mastapy.bearings.bearing_results import _1975

            return self._parent._cast(_1975.LoadedNonLinearBearingResults)

        @property
        def loaded_angular_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2001.LoadedAngularContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2001

            return self._parent._cast(_2001.LoadedAngularContactBallBearingResults)

        @property
        def loaded_angular_contact_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2004.LoadedAngularContactThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2004

            return self._parent._cast(
                _2004.LoadedAngularContactThrustBallBearingResults
            )

        @property
        def loaded_asymmetric_spherical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2007.LoadedAsymmetricSphericalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2007

            return self._parent._cast(
                _2007.LoadedAsymmetricSphericalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2012.LoadedAxialThrustCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2012

            return self._parent._cast(
                _2012.LoadedAxialThrustCylindricalRollerBearingResults
            )

        @property
        def loaded_axial_thrust_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2015.LoadedAxialThrustNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2015

            return self._parent._cast(_2015.LoadedAxialThrustNeedleRollerBearingResults)

        @property
        def loaded_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2020.LoadedBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2020

            return self._parent._cast(_2020.LoadedBallBearingResults)

        @property
        def loaded_crossed_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2023.LoadedCrossedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2023

            return self._parent._cast(_2023.LoadedCrossedRollerBearingResults)

        @property
        def loaded_cylindrical_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2027.LoadedCylindricalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2027

            return self._parent._cast(_2027.LoadedCylindricalRollerBearingResults)

        @property
        def loaded_deep_groove_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2030.LoadedDeepGrooveBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2030

            return self._parent._cast(_2030.LoadedDeepGrooveBallBearingResults)

        @property
        def loaded_four_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2035.LoadedFourPointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2035

            return self._parent._cast(_2035.LoadedFourPointContactBallBearingResults)

        @property
        def loaded_needle_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2039.LoadedNeedleRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2039

            return self._parent._cast(_2039.LoadedNeedleRollerBearingResults)

        @property
        def loaded_non_barrel_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2042.LoadedNonBarrelRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2042

            return self._parent._cast(_2042.LoadedNonBarrelRollerBearingResults)

        @property
        def loaded_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2047.LoadedRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2047

            return self._parent._cast(_2047.LoadedRollerBearingResults)

        @property
        def loaded_rolling_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2051.LoadedRollingBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2051

            return self._parent._cast(_2051.LoadedRollingBearingResults)

        @property
        def loaded_self_aligning_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2054.LoadedSelfAligningBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2054

            return self._parent._cast(_2054.LoadedSelfAligningBallBearingResults)

        @property
        def loaded_spherical_roller_radial_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2058.LoadedSphericalRollerRadialBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2058

            return self._parent._cast(_2058.LoadedSphericalRollerRadialBearingResults)

        @property
        def loaded_spherical_roller_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2061.LoadedSphericalRollerThrustBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2061

            return self._parent._cast(_2061.LoadedSphericalRollerThrustBearingResults)

        @property
        def loaded_taper_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2066.LoadedTaperRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2066

            return self._parent._cast(_2066.LoadedTaperRollerBearingResults)

        @property
        def loaded_three_point_contact_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2069.LoadedThreePointContactBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2069

            return self._parent._cast(_2069.LoadedThreePointContactBallBearingResults)

        @property
        def loaded_thrust_ball_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2072.LoadedThrustBallBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2072

            return self._parent._cast(_2072.LoadedThrustBallBearingResults)

        @property
        def loaded_toroidal_roller_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2075.LoadedToroidalRollerBearingResults":
            from mastapy.bearings.bearing_results.rolling import _2075

            return self._parent._cast(_2075.LoadedToroidalRollerBearingResults)

        @property
        def loaded_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2137.LoadedFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2137

            return self._parent._cast(_2137.LoadedFluidFilmBearingResults)

        @property
        def loaded_grease_filled_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2138.LoadedGreaseFilledJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2138

            return self._parent._cast(_2138.LoadedGreaseFilledJournalBearingResults)

        @property
        def loaded_pad_fluid_film_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2139.LoadedPadFluidFilmBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2139

            return self._parent._cast(_2139.LoadedPadFluidFilmBearingResults)

        @property
        def loaded_plain_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2140.LoadedPlainJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2140

            return self._parent._cast(_2140.LoadedPlainJournalBearingResults)

        @property
        def loaded_plain_oil_fed_journal_bearing(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2142.LoadedPlainOilFedJournalBearing":
            from mastapy.bearings.bearing_results.fluid_film import _2142

            return self._parent._cast(_2142.LoadedPlainOilFedJournalBearing)

        @property
        def loaded_tilting_pad_journal_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2145.LoadedTiltingPadJournalBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2145

            return self._parent._cast(_2145.LoadedTiltingPadJournalBearingResults)

        @property
        def loaded_tilting_pad_thrust_bearing_results(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "_2146.LoadedTiltingPadThrustBearingResults":
            from mastapy.bearings.bearing_results.fluid_film import _2146

            return self._parent._cast(_2146.LoadedTiltingPadThrustBearingResults)

        @property
        def bearing_load_case_results_lightweight(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
        ) -> "BearingLoadCaseResultsLightweight":
            return self._parent

        def __getattr__(
            self: "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "BearingLoadCaseResultsLightweight.TYPE"
    ):
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
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "BearingLoadCaseResultsLightweight._Cast_BearingLoadCaseResultsLightweight":
        return self._Cast_BearingLoadCaseResultsLightweight(self)
