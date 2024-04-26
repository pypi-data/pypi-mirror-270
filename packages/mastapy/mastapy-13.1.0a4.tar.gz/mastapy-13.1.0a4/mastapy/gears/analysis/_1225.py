"""AbstractGearAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.rating import _361, _365, _368
    from mastapy.gears.rating.zerol_bevel import _377
    from mastapy.gears.rating.worm import _379, _381
    from mastapy.gears.rating.straight_bevel import _403
    from mastapy.gears.rating.straight_bevel_diff import _406
    from mastapy.gears.rating.spiral_bevel import _410
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _413
    from mastapy.gears.rating.klingelnberg_hypoid import _416
    from mastapy.gears.rating.klingelnberg_conical import _419
    from mastapy.gears.rating.hypoid import _446
    from mastapy.gears.rating.face import _452, _455
    from mastapy.gears.rating.cylindrical import _462, _467
    from mastapy.gears.rating.conical import _545, _547
    from mastapy.gears.rating.concept import _555, _558
    from mastapy.gears.rating.bevel import _562
    from mastapy.gears.rating.agma_gleason_conical import _573
    from mastapy.gears.manufacturing.cylindrical import _619, _623, _624
    from mastapy.gears.manufacturing.bevel import (
        _782,
        _783,
        _784,
        _785,
        _795,
        _796,
        _801,
    )
    from mastapy.gears.ltca import _847
    from mastapy.gears.ltca.cylindrical import _863
    from mastapy.gears.ltca.conical import _874
    from mastapy.gears.load_case import _880
    from mastapy.gears.load_case.worm import _883
    from mastapy.gears.load_case.face import _886
    from mastapy.gears.load_case.cylindrical import _889
    from mastapy.gears.load_case.conical import _892
    from mastapy.gears.load_case.concept import _895
    from mastapy.gears.load_case.bevel import _898
    from mastapy.gears.gear_two_d_fe_analysis import _905, _906
    from mastapy.gears.gear_designs.face import _1001
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1110,
        _1111,
        _1112,
        _1114,
    )
    from mastapy.gears.fe_model import _1207
    from mastapy.gears.fe_model.cylindrical import _1211
    from mastapy.gears.fe_model.conical import _1214
    from mastapy.gears.analysis import _1228, _1229, _1230, _1231


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearAnalysis",)


Self = TypeVar("Self", bound="AbstractGearAnalysis")


class AbstractGearAnalysis(_0.APIBase):
    """AbstractGearAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearAnalysis")

    class _Cast_AbstractGearAnalysis:
        """Special nested class for casting AbstractGearAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
            parent: "AbstractGearAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_361.AbstractGearRating":
            from mastapy.gears.rating import _361

            return self._parent._cast(_361.AbstractGearRating)

        @property
        def gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_365.GearDutyCycleRating":
            from mastapy.gears.rating import _365

            return self._parent._cast(_365.GearDutyCycleRating)

        @property
        def gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_368.GearRating":
            from mastapy.gears.rating import _368

            return self._parent._cast(_368.GearRating)

        @property
        def zerol_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_377.ZerolBevelGearRating":
            from mastapy.gears.rating.zerol_bevel import _377

            return self._parent._cast(_377.ZerolBevelGearRating)

        @property
        def worm_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_379.WormGearDutyCycleRating":
            from mastapy.gears.rating.worm import _379

            return self._parent._cast(_379.WormGearDutyCycleRating)

        @property
        def worm_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_381.WormGearRating":
            from mastapy.gears.rating.worm import _381

            return self._parent._cast(_381.WormGearRating)

        @property
        def straight_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_403.StraightBevelGearRating":
            from mastapy.gears.rating.straight_bevel import _403

            return self._parent._cast(_403.StraightBevelGearRating)

        @property
        def straight_bevel_diff_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_406.StraightBevelDiffGearRating":
            from mastapy.gears.rating.straight_bevel_diff import _406

            return self._parent._cast(_406.StraightBevelDiffGearRating)

        @property
        def spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_410.SpiralBevelGearRating":
            from mastapy.gears.rating.spiral_bevel import _410

            return self._parent._cast(_410.SpiralBevelGearRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_413.KlingelnbergCycloPalloidSpiralBevelGearRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _413

            return self._parent._cast(
                _413.KlingelnbergCycloPalloidSpiralBevelGearRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_416.KlingelnbergCycloPalloidHypoidGearRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _416

            return self._parent._cast(_416.KlingelnbergCycloPalloidHypoidGearRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_419.KlingelnbergCycloPalloidConicalGearRating":
            from mastapy.gears.rating.klingelnberg_conical import _419

            return self._parent._cast(_419.KlingelnbergCycloPalloidConicalGearRating)

        @property
        def hypoid_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_446.HypoidGearRating":
            from mastapy.gears.rating.hypoid import _446

            return self._parent._cast(_446.HypoidGearRating)

        @property
        def face_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_452.FaceGearDutyCycleRating":
            from mastapy.gears.rating.face import _452

            return self._parent._cast(_452.FaceGearDutyCycleRating)

        @property
        def face_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_455.FaceGearRating":
            from mastapy.gears.rating.face import _455

            return self._parent._cast(_455.FaceGearRating)

        @property
        def cylindrical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_462.CylindricalGearDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _462

            return self._parent._cast(_462.CylindricalGearDutyCycleRating)

        @property
        def cylindrical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_467.CylindricalGearRating":
            from mastapy.gears.rating.cylindrical import _467

            return self._parent._cast(_467.CylindricalGearRating)

        @property
        def conical_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_545.ConicalGearDutyCycleRating":
            from mastapy.gears.rating.conical import _545

            return self._parent._cast(_545.ConicalGearDutyCycleRating)

        @property
        def conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_547.ConicalGearRating":
            from mastapy.gears.rating.conical import _547

            return self._parent._cast(_547.ConicalGearRating)

        @property
        def concept_gear_duty_cycle_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_555.ConceptGearDutyCycleRating":
            from mastapy.gears.rating.concept import _555

            return self._parent._cast(_555.ConceptGearDutyCycleRating)

        @property
        def concept_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_558.ConceptGearRating":
            from mastapy.gears.rating.concept import _558

            return self._parent._cast(_558.ConceptGearRating)

        @property
        def bevel_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_562.BevelGearRating":
            from mastapy.gears.rating.bevel import _562

            return self._parent._cast(_562.BevelGearRating)

        @property
        def agma_gleason_conical_gear_rating(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_573.AGMAGleasonConicalGearRating":
            from mastapy.gears.rating.agma_gleason_conical import _573

            return self._parent._cast(_573.AGMAGleasonConicalGearRating)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_619.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_623.CylindricalManufacturedGearDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_624.CylindricalManufacturedGearLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_782.ConicalGearManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _782

            return self._parent._cast(_782.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_783.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_784.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_795.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_796.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_801.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _801

            return self._parent._cast(_801.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_847.GearLoadDistributionAnalysis":
            from mastapy.gears.ltca import _847

            return self._parent._cast(_847.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_863.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_874.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _874

            return self._parent._cast(_874.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_880.GearLoadCaseBase":
            from mastapy.gears.load_case import _880

            return self._parent._cast(_880.GearLoadCaseBase)

        @property
        def worm_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_883.WormGearLoadCase":
            from mastapy.gears.load_case.worm import _883

            return self._parent._cast(_883.WormGearLoadCase)

        @property
        def face_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_886.FaceGearLoadCase":
            from mastapy.gears.load_case.face import _886

            return self._parent._cast(_886.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_889.CylindricalGearLoadCase":
            from mastapy.gears.load_case.cylindrical import _889

            return self._parent._cast(_889.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_892.ConicalGearLoadCase":
            from mastapy.gears.load_case.conical import _892

            return self._parent._cast(_892.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_895.ConceptGearLoadCase":
            from mastapy.gears.load_case.concept import _895

            return self._parent._cast(_895.ConceptGearLoadCase)

        @property
        def bevel_load_case(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_898.BevelLoadCase":
            from mastapy.gears.load_case.bevel import _898

            return self._parent._cast(_898.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_905.CylindricalGearTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _905

            return self._parent._cast(_905.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_906.CylindricalGearTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _906

            return self._parent._cast(_906.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1001.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1110.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1111.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111

            return self._parent._cast(_1111.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1112.CylindricalGearMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(_1112.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1114.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1207.GearFEModel":
            from mastapy.gears.fe_model import _1207

            return self._parent._cast(_1207.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1211.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1211

            return self._parent._cast(_1211.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1214.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1214

            return self._parent._cast(_1214.ConicalGearFEModel)

        @property
        def gear_design_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def gear_implementation_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1229.GearImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1230.GearImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "_1231.GearImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearImplementationDetail)

        @property
        def abstract_gear_analysis(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis",
        ) -> "AbstractGearAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearAnalysis._Cast_AbstractGearAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def name_with_gear_set_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NameWithGearSetName

        if temp is None:
            return ""

        return temp

    @property
    def planet_index(self: Self) -> "int":
        """int"""
        temp = self.wrapped.PlanetIndex

        if temp is None:
            return 0

        return temp

    @planet_index.setter
    @enforce_parameter_types
    def planet_index(self: Self, value: "int"):
        self.wrapped.PlanetIndex = int(value) if value is not None else 0

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
    def cast_to(self: Self) -> "AbstractGearAnalysis._Cast_AbstractGearAnalysis":
        return self._Cast_AbstractGearAnalysis(self)
