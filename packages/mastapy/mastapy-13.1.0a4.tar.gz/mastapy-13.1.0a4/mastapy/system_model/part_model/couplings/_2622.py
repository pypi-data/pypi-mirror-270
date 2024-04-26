"""SplinePitchErrorOptions"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy.system_model.part_model.couplings import _2621
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import overridable_enum_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_PITCH_ERROR_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "SplinePitchErrorOptions"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2609


__docformat__ = "restructuredtext en"
__all__ = ("SplinePitchErrorOptions",)


Self = TypeVar("Self", bound="SplinePitchErrorOptions")


class SplinePitchErrorOptions(_0.APIBase):
    """SplinePitchErrorOptions

    This is a mastapy class.
    """

    TYPE = _SPLINE_PITCH_ERROR_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplinePitchErrorOptions")

    class _Cast_SplinePitchErrorOptions:
        """Special nested class for casting SplinePitchErrorOptions to subclasses."""

        def __init__(
            self: "SplinePitchErrorOptions._Cast_SplinePitchErrorOptions",
            parent: "SplinePitchErrorOptions",
        ):
            self._parent = parent

        @property
        def spline_pitch_error_options(
            self: "SplinePitchErrorOptions._Cast_SplinePitchErrorOptions",
        ) -> "SplinePitchErrorOptions":
            return self._parent

        def __getattr__(
            self: "SplinePitchErrorOptions._Cast_SplinePitchErrorOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplinePitchErrorOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pitch_error_input_type(
        self: Self,
    ) -> "overridable.Overridable_SplinePitchErrorInputType":
        """Overridable[mastapy.system_model.part_model.couplings.SplinePitchErrorInputType]"""
        temp = self.wrapped.PitchErrorInputType

        if temp is None:
            return None

        value = overridable.Overridable_SplinePitchErrorInputType.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @pitch_error_input_type.setter
    @enforce_parameter_types
    def pitch_error_input_type(
        self: Self,
        value: "Union[_2621.SplinePitchErrorInputType, Tuple[_2621.SplinePitchErrorInputType, bool]]",
    ):
        wrapper_type = overridable.Overridable_SplinePitchErrorInputType.wrapper_type()
        enclosed_type = (
            overridable.Overridable_SplinePitchErrorInputType.implicit_type()
        )
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.PitchErrorInputType = value

    @property
    def pitch_error_options_left_flank(self: Self) -> "_2609.PitchErrorFlankOptions":
        """mastapy.system_model.part_model.couplings.PitchErrorFlankOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchErrorOptionsLeftFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pitch_error_options_right_flank(self: Self) -> "_2609.PitchErrorFlankOptions":
        """mastapy.system_model.part_model.couplings.PitchErrorFlankOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchErrorOptionsRightFlank

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pitch_error_flank_options(self: Self) -> "List[_2609.PitchErrorFlankOptions]":
        """List[mastapy.system_model.part_model.couplings.PitchErrorFlankOptions]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchErrorFlankOptions

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

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
    def cast_to(self: Self) -> "SplinePitchErrorOptions._Cast_SplinePitchErrorOptions":
        return self._Cast_SplinePitchErrorOptions(self)
