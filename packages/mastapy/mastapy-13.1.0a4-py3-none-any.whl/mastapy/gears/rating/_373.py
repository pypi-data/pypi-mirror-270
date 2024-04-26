"""MeshSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MESH_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "MeshSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears import _326
    from mastapy.materials.efficiency import _301
    from mastapy.gears.rating import _371
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _421, _425, _426
    from mastapy.gears.rating.iso_10300 import _429, _430, _431, _432, _433
    from mastapy.gears.rating.hypoid.standards import _450
    from mastapy.gears.rating.cylindrical import _474
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497, _499, _501
    from mastapy.gears.rating.cylindrical.iso6336 import _519, _521, _523, _525, _527
    from mastapy.gears.rating.cylindrical.din3990 import _540
    from mastapy.gears.rating.cylindrical.agma import _542
    from mastapy.gears.rating.conical import _553
    from mastapy.gears.rating.bevel.standards import _565, _567, _569


__docformat__ = "restructuredtext en"
__all__ = ("MeshSingleFlankRating",)


Self = TypeVar("Self", bound="MeshSingleFlankRating")


class MeshSingleFlankRating(_0.APIBase):
    """MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _MESH_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MeshSingleFlankRating")

    class _Cast_MeshSingleFlankRating:
        """Special nested class for casting MeshSingleFlankRating to subclasses."""

        def __init__(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
            parent: "MeshSingleFlankRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_conical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_421.KlingelnbergConicalMeshSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _421

            return self._parent._cast(_421.KlingelnbergConicalMeshSingleFlankRating)

        @property
        def klingelnberg_cyclo_palloid_hypoid_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_425.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _425

            return self._parent._cast(
                _425.KlingelnbergCycloPalloidHypoidMeshSingleFlankRating
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_426.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _426

            return self._parent._cast(
                _426.KlingelnbergCycloPalloidSpiralBevelMeshSingleFlankRating
            )

        @property
        def iso10300_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_429.ISO10300MeshSingleFlankRating":
            from mastapy.gears.rating.iso_10300 import _429

            return self._parent._cast(_429.ISO10300MeshSingleFlankRating)

        @property
        def iso10300_mesh_single_flank_rating_bevel_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_430.ISO10300MeshSingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _430

            return self._parent._cast(_430.ISO10300MeshSingleFlankRatingBevelMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_hypoid_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_431.ISO10300MeshSingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _431

            return self._parent._cast(_431.ISO10300MeshSingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_mesh_single_flank_rating_method_b1(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_432.ISO10300MeshSingleFlankRatingMethodB1":
            from mastapy.gears.rating.iso_10300 import _432

            return self._parent._cast(_432.ISO10300MeshSingleFlankRatingMethodB1)

        @property
        def iso10300_mesh_single_flank_rating_method_b2(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_433.ISO10300MeshSingleFlankRatingMethodB2":
            from mastapy.gears.rating.iso_10300 import _433

            return self._parent._cast(_433.ISO10300MeshSingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_450.GleasonHypoidMeshSingleFlankRating":
            from mastapy.gears.rating.hypoid.standards import _450

            return self._parent._cast(_450.GleasonHypoidMeshSingleFlankRating)

        @property
        def cylindrical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_474.CylindricalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _474

            return self._parent._cast(_474.CylindricalMeshSingleFlankRating)

        @property
        def metal_plastic_or_plastic_metal_vdi2736_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_497.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _497

            return self._parent._cast(
                _497.MetalPlasticOrPlasticMetalVDI2736MeshSingleFlankRating
            )

        @property
        def plastic_gear_vdi2736_abstract_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_499.PlasticGearVDI2736AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _499

            return self._parent._cast(
                _499.PlasticGearVDI2736AbstractMeshSingleFlankRating
            )

        @property
        def plastic_plastic_vdi2736_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_501.PlasticPlasticVDI2736MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _501

            return self._parent._cast(_501.PlasticPlasticVDI2736MeshSingleFlankRating)

        @property
        def iso63361996_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_519.ISO63361996MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _519

            return self._parent._cast(_519.ISO63361996MeshSingleFlankRating)

        @property
        def iso63362006_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_521.ISO63362006MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _521

            return self._parent._cast(_521.ISO63362006MeshSingleFlankRating)

        @property
        def iso63362019_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_523.ISO63362019MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _523

            return self._parent._cast(_523.ISO63362019MeshSingleFlankRating)

        @property
        def iso6336_abstract_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_525.ISO6336AbstractMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _525

            return self._parent._cast(_525.ISO6336AbstractMeshSingleFlankRating)

        @property
        def iso6336_abstract_metal_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_527.ISO6336AbstractMetalMeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _527

            return self._parent._cast(_527.ISO6336AbstractMetalMeshSingleFlankRating)

        @property
        def din3990_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_540.DIN3990MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _540

            return self._parent._cast(_540.DIN3990MeshSingleFlankRating)

        @property
        def agma2101_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_542.AGMA2101MeshSingleFlankRating":
            from mastapy.gears.rating.cylindrical.agma import _542

            return self._parent._cast(_542.AGMA2101MeshSingleFlankRating)

        @property
        def conical_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_553.ConicalMeshSingleFlankRating":
            from mastapy.gears.rating.conical import _553

            return self._parent._cast(_553.ConicalMeshSingleFlankRating)

        @property
        def agma_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_565.AGMASpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _565

            return self._parent._cast(_565.AGMASpiralBevelMeshSingleFlankRating)

        @property
        def gleason_spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_567.GleasonSpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _567

            return self._parent._cast(_567.GleasonSpiralBevelMeshSingleFlankRating)

        @property
        def spiral_bevel_mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "_569.SpiralBevelMeshSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _569

            return self._parent._cast(_569.SpiralBevelMeshSingleFlankRating)

        @property
        def mesh_single_flank_rating(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating",
        ) -> "MeshSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "MeshSingleFlankRating._Cast_MeshSingleFlankRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MeshSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_calculation_method(
        self: Self,
    ) -> "_326.CoefficientOfFrictionCalculationMethod":
        """mastapy.gears.CoefficientOfFrictionCalculationMethod"""
        temp = self.wrapped.CoefficientOfFrictionCalculationMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._326", "CoefficientOfFrictionCalculationMethod"
        )(value)

    @coefficient_of_friction_calculation_method.setter
    @enforce_parameter_types
    def coefficient_of_friction_calculation_method(
        self: Self, value: "_326.CoefficientOfFrictionCalculationMethod"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CoefficientOfFrictionCalculationMethod"
        )
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def efficiency_rating_method(self: Self) -> "_301.EfficiencyRatingMethod":
        """mastapy.materials.efficiency.EfficiencyRatingMethod"""
        temp = self.wrapped.EfficiencyRatingMethod

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.materials.efficiency._301", "EfficiencyRatingMethod"
        )(value)

    @efficiency_rating_method.setter
    @enforce_parameter_types
    def efficiency_rating_method(self: Self, value: "_301.EfficiencyRatingMethod"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Materials.Efficiency.EfficiencyRatingMethod"
        )
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def power(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Power

        if temp is None:
            return 0.0

        return temp

    @property
    def rating_standard_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RatingStandardName

        if temp is None:
            return ""

        return temp

    @property
    def gear_single_flank_ratings(self: Self) -> "List[_371.GearSingleFlankRating]":
        """List[mastapy.gears.rating.GearSingleFlankRating]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSingleFlankRatings

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
    def cast_to(self: Self) -> "MeshSingleFlankRating._Cast_MeshSingleFlankRating":
        return self._Cast_MeshSingleFlankRating(self)
