"""GearSingleFlankRating"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SINGLE_FLANK_RATING = python_net_import(
    "SMT.MastaAPI.Gears.Rating", "GearSingleFlankRating"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.klingelnberg_conical.kn3030 import _423, _424
    from mastapy.gears.rating.iso_10300 import _436, _437, _438, _439, _440
    from mastapy.gears.rating.hypoid.standards import _449
    from mastapy.gears.rating.cylindrical import _472
    from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498, _503, _504
    from mastapy.gears.rating.cylindrical.iso6336 import _518, _520, _522, _524, _526
    from mastapy.gears.rating.cylindrical.din3990 import _539
    from mastapy.gears.rating.cylindrical.agma import _541
    from mastapy.gears.rating.conical import _550
    from mastapy.gears.rating.bevel.standards import _564, _566, _568


__docformat__ = "restructuredtext en"
__all__ = ("GearSingleFlankRating",)


Self = TypeVar("Self", bound="GearSingleFlankRating")


class GearSingleFlankRating(_0.APIBase):
    """GearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SINGLE_FLANK_RATING
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSingleFlankRating")

    class _Cast_GearSingleFlankRating:
        """Special nested class for casting GearSingleFlankRating to subclasses."""

        def __init__(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
            parent: "GearSingleFlankRating",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_423.KlingelnbergCycloPalloidConicalGearSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _423

            return self._parent._cast(
                _423.KlingelnbergCycloPalloidConicalGearSingleFlankRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_424.KlingelnbergCycloPalloidHypoidGearSingleFlankRating":
            from mastapy.gears.rating.klingelnberg_conical.kn3030 import _424

            return self._parent._cast(
                _424.KlingelnbergCycloPalloidHypoidGearSingleFlankRating
            )

        @property
        def iso10300_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_436.ISO10300SingleFlankRating":
            from mastapy.gears.rating.iso_10300 import _436

            return self._parent._cast(_436.ISO10300SingleFlankRating)

        @property
        def iso10300_single_flank_rating_bevel_method_b2(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_437.ISO10300SingleFlankRatingBevelMethodB2":
            from mastapy.gears.rating.iso_10300 import _437

            return self._parent._cast(_437.ISO10300SingleFlankRatingBevelMethodB2)

        @property
        def iso10300_single_flank_rating_hypoid_method_b2(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_438.ISO10300SingleFlankRatingHypoidMethodB2":
            from mastapy.gears.rating.iso_10300 import _438

            return self._parent._cast(_438.ISO10300SingleFlankRatingHypoidMethodB2)

        @property
        def iso10300_single_flank_rating_method_b1(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_439.ISO10300SingleFlankRatingMethodB1":
            from mastapy.gears.rating.iso_10300 import _439

            return self._parent._cast(_439.ISO10300SingleFlankRatingMethodB1)

        @property
        def iso10300_single_flank_rating_method_b2(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_440.ISO10300SingleFlankRatingMethodB2":
            from mastapy.gears.rating.iso_10300 import _440

            return self._parent._cast(_440.ISO10300SingleFlankRatingMethodB2)

        @property
        def gleason_hypoid_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_449.GleasonHypoidGearSingleFlankRating":
            from mastapy.gears.rating.hypoid.standards import _449

            return self._parent._cast(_449.GleasonHypoidGearSingleFlankRating)

        @property
        def cylindrical_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_472.CylindricalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical import _472

            return self._parent._cast(_472.CylindricalGearSingleFlankRating)

        @property
        def plastic_gear_vdi2736_abstract_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_498.PlasticGearVDI2736AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _498

            return self._parent._cast(
                _498.PlasticGearVDI2736AbstractGearSingleFlankRating
            )

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_metal_plastic_or_a_plastic_metal_mesh(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> (
            "_503.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh"
        ):
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _503

            return self._parent._cast(
                _503.PlasticVDI2736GearSingleFlankRatingInAMetalPlasticOrAPlasticMetalMesh
            )

        @property
        def plastic_vdi2736_gear_single_flank_rating_in_a_plastic_plastic_mesh(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_504.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh":
            from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _504

            return self._parent._cast(
                _504.PlasticVDI2736GearSingleFlankRatingInAPlasticPlasticMesh
            )

        @property
        def iso63361996_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_518.ISO63361996GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _518

            return self._parent._cast(_518.ISO63361996GearSingleFlankRating)

        @property
        def iso63362006_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_520.ISO63362006GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _520

            return self._parent._cast(_520.ISO63362006GearSingleFlankRating)

        @property
        def iso63362019_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_522.ISO63362019GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _522

            return self._parent._cast(_522.ISO63362019GearSingleFlankRating)

        @property
        def iso6336_abstract_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_524.ISO6336AbstractGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _524

            return self._parent._cast(_524.ISO6336AbstractGearSingleFlankRating)

        @property
        def iso6336_abstract_metal_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_526.ISO6336AbstractMetalGearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.iso6336 import _526

            return self._parent._cast(_526.ISO6336AbstractMetalGearSingleFlankRating)

        @property
        def din3990_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_539.DIN3990GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.din3990 import _539

            return self._parent._cast(_539.DIN3990GearSingleFlankRating)

        @property
        def agma2101_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_541.AGMA2101GearSingleFlankRating":
            from mastapy.gears.rating.cylindrical.agma import _541

            return self._parent._cast(_541.AGMA2101GearSingleFlankRating)

        @property
        def conical_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_550.ConicalGearSingleFlankRating":
            from mastapy.gears.rating.conical import _550

            return self._parent._cast(_550.ConicalGearSingleFlankRating)

        @property
        def agma_spiral_bevel_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_564.AGMASpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _564

            return self._parent._cast(_564.AGMASpiralBevelGearSingleFlankRating)

        @property
        def gleason_spiral_bevel_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_566.GleasonSpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _566

            return self._parent._cast(_566.GleasonSpiralBevelGearSingleFlankRating)

        @property
        def spiral_bevel_gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "_568.SpiralBevelGearSingleFlankRating":
            from mastapy.gears.rating.bevel.standards import _568

            return self._parent._cast(_568.SpiralBevelGearSingleFlankRating)

        @property
        def gear_single_flank_rating(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating",
        ) -> "GearSingleFlankRating":
            return self._parent

        def __getattr__(
            self: "GearSingleFlankRating._Cast_GearSingleFlankRating", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSingleFlankRating.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Duration

        if temp is None:
            return 0.0

        return temp

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
    def number_of_load_cycles(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfLoadCycles

        if temp is None:
            return 0.0

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
    def rotation_speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RotationSpeed

        if temp is None:
            return 0.0

        return temp

    @property
    def torque(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Torque

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
    def cast_to(self: Self) -> "GearSingleFlankRating._Cast_GearSingleFlankRating":
        return self._Cast_GearSingleFlankRating(self)
