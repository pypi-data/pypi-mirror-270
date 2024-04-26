"""Modification"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MODIFICATION = python_net_import("SMT.MastaAPI.Gears.MicroGeometry", "Modification")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical import _1030
    from mastapy.gears.micro_geometry import _576, _579, _589
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1103,
        _1106,
        _1107,
        _1115,
        _1116,
        _1120,
    )
    from mastapy.gears.gear_designs.conical.micro_geometry import _1182, _1184, _1185


__docformat__ = "restructuredtext en"
__all__ = ("Modification",)


Self = TypeVar("Self", bound="Modification")


class Modification(_0.APIBase):
    """Modification

    This is a mastapy class.
    """

    TYPE = _MODIFICATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Modification")

    class _Cast_Modification:
        """Special nested class for casting Modification to subclasses."""

        def __init__(self: "Modification._Cast_Modification", parent: "Modification"):
            self._parent = parent

        @property
        def bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_576.BiasModification":
            from mastapy.gears.micro_geometry import _576

            return self._parent._cast(_576.BiasModification)

        @property
        def lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_579.LeadModification":
            from mastapy.gears.micro_geometry import _579

            return self._parent._cast(_579.LeadModification)

        @property
        def profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_589.ProfileModification":
            from mastapy.gears.micro_geometry import _589

            return self._parent._cast(_589.ProfileModification)

        @property
        def cylindrical_gear_bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1103.CylindricalGearBiasModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1103

            return self._parent._cast(_1103.CylindricalGearBiasModification)

        @property
        def cylindrical_gear_lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1106.CylindricalGearLeadModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1106

            return self._parent._cast(_1106.CylindricalGearLeadModification)

        @property
        def cylindrical_gear_lead_modification_at_profile_position(
            self: "Modification._Cast_Modification",
        ) -> "_1107.CylindricalGearLeadModificationAtProfilePosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1107

            return self._parent._cast(
                _1107.CylindricalGearLeadModificationAtProfilePosition
            )

        @property
        def cylindrical_gear_profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1115.CylindricalGearProfileModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1115

            return self._parent._cast(_1115.CylindricalGearProfileModification)

        @property
        def cylindrical_gear_profile_modification_at_face_width_position(
            self: "Modification._Cast_Modification",
        ) -> "_1116.CylindricalGearProfileModificationAtFaceWidthPosition":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1116

            return self._parent._cast(
                _1116.CylindricalGearProfileModificationAtFaceWidthPosition
            )

        @property
        def cylindrical_gear_triangular_end_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1120.CylindricalGearTriangularEndModification":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1120

            return self._parent._cast(_1120.CylindricalGearTriangularEndModification)

        @property
        def conical_gear_bias_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1182.ConicalGearBiasModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1182

            return self._parent._cast(_1182.ConicalGearBiasModification)

        @property
        def conical_gear_lead_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1184.ConicalGearLeadModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1184

            return self._parent._cast(_1184.ConicalGearLeadModification)

        @property
        def conical_gear_profile_modification(
            self: "Modification._Cast_Modification",
        ) -> "_1185.ConicalGearProfileModification":
            from mastapy.gears.gear_designs.conical.micro_geometry import _1185

            return self._parent._cast(_1185.ConicalGearProfileModification)

        @property
        def modification(self: "Modification._Cast_Modification") -> "Modification":
            return self._parent

        def __getattr__(self: "Modification._Cast_Modification", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Modification.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def settings(self: Self) -> "_1030.CylindricalGearMicroGeometrySettingsItem":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearMicroGeometrySettingsItem

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Settings

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cast_to(self: Self) -> "Modification._Cast_Modification":
        return self._Cast_Modification(self)
