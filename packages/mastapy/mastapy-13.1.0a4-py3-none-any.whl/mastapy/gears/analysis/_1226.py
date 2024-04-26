"""AbstractGearMeshAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_GEAR_MESH_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "AbstractGearMeshAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1225, _1232, _1233, _1234, _1235
    from mastapy.gears.rating import _360, _367, _372
    from mastapy.gears.rating.zerol_bevel import _376
    from mastapy.gears.rating.worm import _380, _384
    from mastapy.gears.rating.straight_bevel import _402
    from mastapy.gears.rating.straight_bevel_diff import _405
    from mastapy.gears.rating.spiral_bevel import _409
    from mastapy.gears.rating.klingelnberg_spiral_bevel import _412
    from mastapy.gears.rating.klingelnberg_hypoid import _415
    from mastapy.gears.rating.klingelnberg_conical import _418
    from mastapy.gears.rating.hypoid import _445
    from mastapy.gears.rating.face import _453, _454
    from mastapy.gears.rating.cylindrical import _465, _473
    from mastapy.gears.rating.conical import _546, _551
    from mastapy.gears.rating.concept import _556, _557
    from mastapy.gears.rating.bevel import _561
    from mastapy.gears.rating.agma_gleason_conical import _572
    from mastapy.gears.manufacturing.cylindrical import _625, _626, _629
    from mastapy.gears.manufacturing.bevel import _791, _792, _793, _794
    from mastapy.gears.ltca import _848
    from mastapy.gears.ltca.cylindrical import _864
    from mastapy.gears.ltca.conical import _877
    from mastapy.gears.load_case import _882
    from mastapy.gears.load_case.worm import _885
    from mastapy.gears.load_case.face import _888
    from mastapy.gears.load_case.cylindrical import _891
    from mastapy.gears.load_case.conical import _894
    from mastapy.gears.load_case.concept import _897
    from mastapy.gears.load_case.bevel import _899
    from mastapy.gears.gear_two_d_fe_analysis import _901, _902
    from mastapy.gears.gear_designs.face import _1000
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108, _1109
    from mastapy.gears.fe_model import _1208
    from mastapy.gears.fe_model.cylindrical import _1212
    from mastapy.gears.fe_model.conical import _1215


__docformat__ = "restructuredtext en"
__all__ = ("AbstractGearMeshAnalysis",)


Self = TypeVar("Self", bound="AbstractGearMeshAnalysis")


class AbstractGearMeshAnalysis(_0.APIBase):
    """AbstractGearMeshAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_GEAR_MESH_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractGearMeshAnalysis")

    class _Cast_AbstractGearMeshAnalysis:
        """Special nested class for casting AbstractGearMeshAnalysis to subclasses."""

        def __init__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
            parent: "AbstractGearMeshAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_360.AbstractGearMeshRating":
            from mastapy.gears.rating import _360

            return self._parent._cast(_360.AbstractGearMeshRating)

        @property
        def gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_367.GearMeshRating":
            from mastapy.gears.rating import _367

            return self._parent._cast(_367.GearMeshRating)

        @property
        def mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_372.MeshDutyCycleRating":
            from mastapy.gears.rating import _372

            return self._parent._cast(_372.MeshDutyCycleRating)

        @property
        def zerol_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_376.ZerolBevelGearMeshRating":
            from mastapy.gears.rating.zerol_bevel import _376

            return self._parent._cast(_376.ZerolBevelGearMeshRating)

        @property
        def worm_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_380.WormGearMeshRating":
            from mastapy.gears.rating.worm import _380

            return self._parent._cast(_380.WormGearMeshRating)

        @property
        def worm_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_384.WormMeshDutyCycleRating":
            from mastapy.gears.rating.worm import _384

            return self._parent._cast(_384.WormMeshDutyCycleRating)

        @property
        def straight_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_402.StraightBevelGearMeshRating":
            from mastapy.gears.rating.straight_bevel import _402

            return self._parent._cast(_402.StraightBevelGearMeshRating)

        @property
        def straight_bevel_diff_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_405.StraightBevelDiffGearMeshRating":
            from mastapy.gears.rating.straight_bevel_diff import _405

            return self._parent._cast(_405.StraightBevelDiffGearMeshRating)

        @property
        def spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_409.SpiralBevelGearMeshRating":
            from mastapy.gears.rating.spiral_bevel import _409

            return self._parent._cast(_409.SpiralBevelGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_412.KlingelnbergCycloPalloidSpiralBevelGearMeshRating":
            from mastapy.gears.rating.klingelnberg_spiral_bevel import _412

            return self._parent._cast(
                _412.KlingelnbergCycloPalloidSpiralBevelGearMeshRating
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_415.KlingelnbergCycloPalloidHypoidGearMeshRating":
            from mastapy.gears.rating.klingelnberg_hypoid import _415

            return self._parent._cast(_415.KlingelnbergCycloPalloidHypoidGearMeshRating)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_418.KlingelnbergCycloPalloidConicalGearMeshRating":
            from mastapy.gears.rating.klingelnberg_conical import _418

            return self._parent._cast(
                _418.KlingelnbergCycloPalloidConicalGearMeshRating
            )

        @property
        def hypoid_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_445.HypoidGearMeshRating":
            from mastapy.gears.rating.hypoid import _445

            return self._parent._cast(_445.HypoidGearMeshRating)

        @property
        def face_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_453.FaceGearMeshDutyCycleRating":
            from mastapy.gears.rating.face import _453

            return self._parent._cast(_453.FaceGearMeshDutyCycleRating)

        @property
        def face_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_454.FaceGearMeshRating":
            from mastapy.gears.rating.face import _454

            return self._parent._cast(_454.FaceGearMeshRating)

        @property
        def cylindrical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_465.CylindricalGearMeshRating":
            from mastapy.gears.rating.cylindrical import _465

            return self._parent._cast(_465.CylindricalGearMeshRating)

        @property
        def cylindrical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_473.CylindricalMeshDutyCycleRating":
            from mastapy.gears.rating.cylindrical import _473

            return self._parent._cast(_473.CylindricalMeshDutyCycleRating)

        @property
        def conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_546.ConicalGearMeshRating":
            from mastapy.gears.rating.conical import _546

            return self._parent._cast(_546.ConicalGearMeshRating)

        @property
        def conical_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_551.ConicalMeshDutyCycleRating":
            from mastapy.gears.rating.conical import _551

            return self._parent._cast(_551.ConicalMeshDutyCycleRating)

        @property
        def concept_gear_mesh_duty_cycle_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_556.ConceptGearMeshDutyCycleRating":
            from mastapy.gears.rating.concept import _556

            return self._parent._cast(_556.ConceptGearMeshDutyCycleRating)

        @property
        def concept_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_557.ConceptGearMeshRating":
            from mastapy.gears.rating.concept import _557

            return self._parent._cast(_557.ConceptGearMeshRating)

        @property
        def bevel_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_561.BevelGearMeshRating":
            from mastapy.gears.rating.bevel import _561

            return self._parent._cast(_561.BevelGearMeshRating)

        @property
        def agma_gleason_conical_gear_mesh_rating(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_572.AGMAGleasonConicalGearMeshRating":
            from mastapy.gears.rating.agma_gleason_conical import _572

            return self._parent._cast(_572.AGMAGleasonConicalGearMeshRating)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_625.CylindricalManufacturedGearMeshDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_626.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_629.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(_629.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_791.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_792.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_793.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_794.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_848.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _848

            return self._parent._cast(_848.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_864.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _864

            return self._parent._cast(_864.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_877.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _877

            return self._parent._cast(_877.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_882.MeshLoadCase":
            from mastapy.gears.load_case import _882

            return self._parent._cast(_882.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_885.WormMeshLoadCase":
            from mastapy.gears.load_case.worm import _885

            return self._parent._cast(_885.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_888.FaceMeshLoadCase":
            from mastapy.gears.load_case.face import _888

            return self._parent._cast(_888.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_891.CylindricalMeshLoadCase":
            from mastapy.gears.load_case.cylindrical import _891

            return self._parent._cast(_891.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_894.ConicalMeshLoadCase":
            from mastapy.gears.load_case.conical import _894

            return self._parent._cast(_894.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_897.ConceptMeshLoadCase":
            from mastapy.gears.load_case.concept import _897

            return self._parent._cast(_897.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_899.BevelMeshLoadCase":
            from mastapy.gears.load_case.bevel import _899

            return self._parent._cast(_899.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_901.CylindricalGearMeshTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _901

            return self._parent._cast(_901.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_902.CylindricalGearMeshTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _902

            return self._parent._cast(_902.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1000.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _1000

            return self._parent._cast(_1000.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1108.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1109.CylindricalGearMeshMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1109

            return self._parent._cast(_1109.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1208.GearMeshFEModel":
            from mastapy.gears.fe_model import _1208

            return self._parent._cast(_1208.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1212.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1212

            return self._parent._cast(_1212.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1215.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1215

            return self._parent._cast(_1215.ConicalMeshFEModel)

        @property
        def gear_mesh_design_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1232.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearMeshDesignAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1233.GearMeshImplementationAnalysis":
            from mastapy.gears.analysis import _1233

            return self._parent._cast(_1233.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1234.GearMeshImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1234

            return self._parent._cast(_1234.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "_1235.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearMeshImplementationDetail)

        @property
        def abstract_gear_mesh_analysis(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis",
        ) -> "AbstractGearMeshAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractGearMeshAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshName

        if temp is None:
            return ""

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
    def gear_a(self: Self) -> "_1225.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1225.AbstractGearAnalysis":
        """mastapy.gears.analysis.AbstractGearAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

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
    def cast_to(
        self: Self,
    ) -> "AbstractGearMeshAnalysis._Cast_AbstractGearMeshAnalysis":
        return self._Cast_AbstractGearMeshAnalysis(self)
