"""AbstractAnalysisOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ANALYSIS_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "AbstractAnalysisOptions",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6830
    from mastapy.system_model.analyses_and_results.system_deflections import _2850
    from mastapy.system_model.analyses_and_results.modal_analyses import _4657
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5486
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5778,
        _5837,
        _5844,
    )


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAnalysisOptions",)


Self = TypeVar("Self", bound="AbstractAnalysisOptions")
T = TypeVar("T", bound="_6830.LoadCase")


class AbstractAnalysisOptions(_0.APIBase, Generic[T]):
    """AbstractAnalysisOptions

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ABSTRACT_ANALYSIS_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAnalysisOptions")

    class _Cast_AbstractAnalysisOptions:
        """Special nested class for casting AbstractAnalysisOptions to subclasses."""

        def __init__(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
            parent: "AbstractAnalysisOptions",
        ):
            self._parent = parent

        @property
        def system_deflection_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_2850.SystemDeflectionOptions":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2850,
            )

            return self._parent._cast(_2850.SystemDeflectionOptions)

        @property
        def frequency_response_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_4657.FrequencyResponseAnalysisOptions":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4657

            return self._parent._cast(_4657.FrequencyResponseAnalysisOptions)

        @property
        def mbd_run_up_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5486.MBDRunUpAnalysisOptions":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5486

            return self._parent._cast(_5486.MBDRunUpAnalysisOptions)

        @property
        def frequency_options_for_harmonic_analysis_results(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5778.FrequencyOptionsForHarmonicAnalysisResults":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5778,
            )

            return self._parent._cast(_5778.FrequencyOptionsForHarmonicAnalysisResults)

        @property
        def speed_options_for_harmonic_analysis_results(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5837.SpeedOptionsForHarmonicAnalysisResults":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5837,
            )

            return self._parent._cast(_5837.SpeedOptionsForHarmonicAnalysisResults)

        @property
        def stiffness_options_for_harmonic_analysis(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "_5844.StiffnessOptionsForHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5844,
            )

            return self._parent._cast(_5844.StiffnessOptionsForHarmonicAnalysis)

        @property
        def abstract_analysis_options(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions",
        ) -> "AbstractAnalysisOptions":
            return self._parent

        def __getattr__(
            self: "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAnalysisOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "AbstractAnalysisOptions._Cast_AbstractAnalysisOptions":
        return self._Cast_AbstractAnalysisOptions(self)
