"""AbstractGearSetAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_SET_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearSetAnalysis"
)

if TYPE_CHECKING:
    from mastapy.utility.model_validation import _1807, _1806
    from mastapy.gears.rating import _362, _369, _370
    from mastapy.gears.rating.zerol_bevel import _378
    from mastapy.gears.rating.worm import _382, _383
    from mastapy.gears.rating.straight_bevel import _404
    from mastapy.gears.rating.straight_bevel_diff import _407
    from mastapy.gears.rating.spiral_bevel import _411
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _414
    from mastapy.gears.rating.klingelnberg_hypoid import _417
    from mastapy.gears.rating.klingelnberg_conical import _420
    from mastapy.gears.rating.hypoid import _447
    from mastapy.gears.rating.face import _456, _457
    from mastapy.gears.rating.cylindrical import _470, _471, _487
    from mastapy.gears.rating.conical import _548, _549
    from mastapy.gears.rating.concept import _559, _560
    from mastapy.gears.rating.bevel import _563
    from mastapy.gears.rating.agma_gleason_conical import _574
    from mastapy.gears.manufacturing.cylindrical import _627, _628, _632
    from mastapy.gears.manufacturing.bevel import _797, _798, _799, _800
    from mastapy.gears.ltca import _853
    from mastapy.gears.ltca.cylindrical import _867, _869
    from mastapy.gears.ltca.conical import _875
    from mastapy.gears.load_case import _881
    from mastapy.gears.load_case.worm import _884
    from mastapy.gears.load_case.face import _887
    from mastapy.gears.load_case.cylindrical import _890
    from mastapy.gears.load_case.conical import _893
    from mastapy.gears.load_case.concept import _896
    from mastapy.gears.load_case.bevel import _900
    from mastapy.gears.gear_two_d_fe_analysis import _903, _904
    from mastapy.gears.gear_designs.face import _1004
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1117, _1118
    from mastapy.gears.fe_model import _1210
    from mastapy.gears.fe_model.cylindrical import _1213
    from mastapy.gears.fe_model.conical import _1216
    from mastapy.gears.analysis import _1236, _1238, _1239, _1240, _1241


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearSetAnalysis",)


Self = TypeVar("Self", bound="AbstractGearSetAnalysis")


class AbstractGearSetAnalysis(_0.APIBase):
    """AbstractGearSetAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_SET_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearSetAnalysis")

    class _Cast_AbstractGearSetAnalysis:
        """Special nested class for casting AbstractGearSetAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
            parent: "AbstractGearSetAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_362.AbstractGearSetRating":
            from mastapy.gears.rating import _362

            return self._parent._cast(_362.AbstractGearSetRating)

        @property
        def gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_369.GearSetDutyCycleRating":
            from mastapy.gears.rating import _369

            return self._parent._cast(_369.GearSetDutyCycleRating)

        @property
        def gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_370.GearSetRating":
            from mastapy.gears.rating import _370

            return self._parent._cast(_370.GearSetRating)

        @property
        def zerol_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_378.ZerolBevelGearSetRating":
            from mastapy.gears.rating.zerol_bevel import _378

            return self._parent._cast(_378.ZerolBevelGearSetRating)

        @property
        def worm_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_382.WormGearSetDutyCycleRating":
            from mastapy.gears.rating.worm import _382

            return self._parent._cast(_382.WormGearSetDutyCycleRating)

        @property
        def worm_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_383.WormGearSetRating":
            from mastapy.gears.rating.worm import _383

            return self._parent._cast(_383.WormGearSetRating)

        @property
        def straight_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_404.StraightBevelGearSetRating":
            from mastapy.gears.rating.straight_bevel import _404

            return self._parent._cast(_404.StraightBevelGearSetRating)

        @property
        def straight_bevel_diff_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_407.StraightBevelDiffGearSetRating":
            from mastapy.gears.rating.straight_bevel_diff import _407

            return self._parent._cast(_407.StraightBevelDiffGearSetRating)

        @property
        def spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_411.SpiralBevelGearSetRating":
            from mastapy.gears.rating.spiral_bevel import _411

            return self._parent._cast(_411.SpiralBevelGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_414.KlingelnbergCycloPalloidSpiralBevelGearSetRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _414

            return self._parent._cast(
                _414.KlingelnbergCycloPalloidSpiralBevelGearSetRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_417.KlingelnbergCycloPalloidHypoidGearSetRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _417

            return self._parent._cast(_417.KlingelnbergCycloPalloidHypoidGearSetRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_420.KlingelnbergCycloPalloidConicalGearSetRating":
            from mastapy.gears.rating.klingelnberg_conical import _420

            return self._parent._cast(_420.KlingelnbergCycloPalloidConicalGearSetRating)

        @property
        def hypoid_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_447.HypoidGearSetRating":
            from mastapy.gears.rating.hypoid import _447

            return self._parent._cast(_447.HypoidGearSetRating)

        @property
        def face_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_456.FaceGearSetDutyCycleRating":
            from mastapy.gears.rating.face import _456

            return self._parent._cast(_456.FaceGearSetDutyCycleRating)

        @property
        def face_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_457.FaceGearSetRating":
            from mastapy.gears.rating.face import _457

            return self._parent._cast(_457.FaceGearSetRating)

        @property
        def cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_470.CylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _470

            return self._parent._cast(_470.CylindricalGearSetDutyCycleRating)

        @property
        def cylindrical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_471.CylindricalGearSetRating":
            from mastapy.gears.rating.cylindrical import _471

            return self._parent._cast(_471.CylindricalGearSetRating)

        @property
        def reduced_cylindrical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_487.ReducedCylindricalGearSetDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _487

            return self._parent._cast(_487.ReducedCylindricalGearSetDutyCycleRating)

        @property
        def conical_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_548.ConicalGearSetDutyCycleRating":
            from mastapy.gears.rating.conical import _548

            return self._parent._cast(_548.ConicalGearSetDutyCycleRating)

        @property
        def conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_549.ConicalGearSetRating":
            from mastapy.gears.rating.conical import _549

            return self._parent._cast(_549.ConicalGearSetRating)

        @property
        def concept_gear_set_duty_cycle_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_559.ConceptGearSetDutyCycleRating":
            from mastapy.gears.rating.concept import _559

            return self._parent._cast(_559.ConceptGearSetDutyCycleRating)

        @property
        def concept_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_560.ConceptGearSetRating":
            from mastapy.gears.rating.concept import _560

            return self._parent._cast(_560.ConceptGearSetRating)

        @property
        def bevel_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_563.BevelGearSetRating":
            from mastapy.gears.rating.bevel import _563

            return self._parent._cast(_563.BevelGearSetRating)

        @property
        def agma_gleason_conical_gear_set_rating(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_574.AGMAGleasonConicalGearSetRating":
            from mastapy.gears.rating.agma_gleason_conical import _574

            return self._parent._cast(_574.AGMAGleasonConicalGearSetRating)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_627.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _627

            return self._parent._cast(_627.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_628.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_632.CylindricalSetManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _632

            return self._parent._cast(_632.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_797.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_798.ConicalSetManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _798

            return self._parent._cast(_798.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_799.ConicalSetMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _799

            return self._parent._cast(_799.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_800.ConicalSetMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _800

            return self._parent._cast(_800.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_853.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _853

            return self._parent._cast(_853.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_867.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _867

            return self._parent._cast(_867.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_869.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _869

            return self._parent._cast(_869.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_875.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_881.GearSetLoadCaseBase":
            from mastapy.gears.load_case import _881

            return self._parent._cast(_881.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_884.WormGearSetLoadCase":
            from mastapy.gears.load_case.worm import _884

            return self._parent._cast(_884.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_887.FaceGearSetLoadCase":
            from mastapy.gears.load_case.face import _887

            return self._parent._cast(_887.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_890.CylindricalGearSetLoadCase":
            from mastapy.gears.load_case.cylindrical import _890

            return self._parent._cast(_890.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_893.ConicalGearSetLoadCase":
            from mastapy.gears.load_case.conical import _893

            return self._parent._cast(_893.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_896.ConceptGearSetLoadCase":
            from mastapy.gears.load_case.concept import _896

            return self._parent._cast(_896.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_900.BevelSetLoadCase":
            from mastapy.gears.load_case.bevel import _900

            return self._parent._cast(_900.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_903.CylindricalGearSetTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _903

            return self._parent._cast(_903.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_904.CylindricalGearSetTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _904

            return self._parent._cast(_904.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1004.FaceGearSetMicroGeometry":
            from mastapy.gears.gear_designs.face import _1004

            return self._parent._cast(_1004.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1117.CylindricalGearSetMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1117

            return self._parent._cast(_1117.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1118.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118

            return self._parent._cast(_1118.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1210.GearSetFEModel":
            from mastapy.gears.fe_model import _1210

            return self._parent._cast(_1210.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1213.CylindricalGearSetFEModel":
            from mastapy.gears.fe_model.cylindrical import _1213

            return self._parent._cast(_1213.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1216.ConicalSetFEModel":
            from mastapy.gears.fe_model.conical import _1216

            return self._parent._cast(_1216.ConicalSetFEModel)

        @property
        def gear_set_design_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1238.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1238

            return self._parent._cast(_1238.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1239.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1239

            return self._parent._cast(_1239.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1240.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1240

            return self._parent._cast(_1240.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "_1241.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1241

            return self._parent._cast(_1241.GearSetImplementationDetail)

        @property
        def abstract_gear_set_analysis(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis",
        ) -> "AbstractGearSetAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearSetAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def all_status_errors(self: Self) -> "List[_1807.StatusItem]":
        """List[mastapy.utility.model_validation.StatusItem]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllStatusErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def status(self: Self) -> "_1806.Status":
        """mastapy.utility.model_validation.Status

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Status

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
    def cast_to(self: Self) -> "AbstractGearSetAnalysis._Cast_AbstractGearSetAnalysis":
        return self._Cast_AbstractGearSetAnalysis(self)
