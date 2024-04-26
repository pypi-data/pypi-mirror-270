"""GearSetDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1227
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetDesignAnalysis"
)

if TYPE_CHECKING:
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
    from mastapy.gears.analysis import _1238, _1239, _1240, _1241


__docformat__ = "restructuredtext en"
__all__ = ("GearSetDesignAnalysis",)


Self = TypeVar("Self", bound="GearSetDesignAnalysis")


class GearSetDesignAnalysis(_1227.AbstractGearSetAnalysis):
    """GearSetDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetDesignAnalysis")

    class _Cast_GearSetDesignAnalysis:
        """Special nested class for casting GearSetDesignAnalysis to subclasses."""

        def __init__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
            parent: "GearSetDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_set_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1227.AbstractGearSetAnalysis":
            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_627.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _627

            return self._parent._cast(_627.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_628.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalManufacturedGearSetLoadCase)

        @property
        def cylindrical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_632.CylindricalSetManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _632

            return self._parent._cast(_632.CylindricalSetManufacturingConfig)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_797.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalSetManufacturingAnalysis)

        @property
        def conical_set_manufacturing_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_798.ConicalSetManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _798

            return self._parent._cast(_798.ConicalSetManufacturingConfig)

        @property
        def conical_set_micro_geometry_config(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_799.ConicalSetMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _799

            return self._parent._cast(_799.ConicalSetMicroGeometryConfig)

        @property
        def conical_set_micro_geometry_config_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_800.ConicalSetMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _800

            return self._parent._cast(_800.ConicalSetMicroGeometryConfigBase)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_853.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _853

            return self._parent._cast(_853.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_867.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _867

            return self._parent._cast(_867.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_869.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _869

            return self._parent._cast(_869.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_875.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_case_base(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_881.GearSetLoadCaseBase":
            from mastapy.gears.load_case import _881

            return self._parent._cast(_881.GearSetLoadCaseBase)

        @property
        def worm_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_884.WormGearSetLoadCase":
            from mastapy.gears.load_case.worm import _884

            return self._parent._cast(_884.WormGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_887.FaceGearSetLoadCase":
            from mastapy.gears.load_case.face import _887

            return self._parent._cast(_887.FaceGearSetLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_890.CylindricalGearSetLoadCase":
            from mastapy.gears.load_case.cylindrical import _890

            return self._parent._cast(_890.CylindricalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_893.ConicalGearSetLoadCase":
            from mastapy.gears.load_case.conical import _893

            return self._parent._cast(_893.ConicalGearSetLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_896.ConceptGearSetLoadCase":
            from mastapy.gears.load_case.concept import _896

            return self._parent._cast(_896.ConceptGearSetLoadCase)

        @property
        def bevel_set_load_case(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_900.BevelSetLoadCase":
            from mastapy.gears.load_case.bevel import _900

            return self._parent._cast(_900.BevelSetLoadCase)

        @property
        def cylindrical_gear_set_tiff_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_903.CylindricalGearSetTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _903

            return self._parent._cast(_903.CylindricalGearSetTIFFAnalysis)

        @property
        def cylindrical_gear_set_tiff_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_904.CylindricalGearSetTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _904

            return self._parent._cast(_904.CylindricalGearSetTIFFAnalysisDutyCycle)

        @property
        def face_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1004.FaceGearSetMicroGeometry":
            from mastapy.gears.gear_designs.face import _1004

            return self._parent._cast(_1004.FaceGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1117.CylindricalGearSetMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1117

            return self._parent._cast(_1117.CylindricalGearSetMicroGeometry)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1118.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118

            return self._parent._cast(_1118.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1210.GearSetFEModel":
            from mastapy.gears.fe_model import _1210

            return self._parent._cast(_1210.GearSetFEModel)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1213.CylindricalGearSetFEModel":
            from mastapy.gears.fe_model.cylindrical import _1213

            return self._parent._cast(_1213.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1216.ConicalSetFEModel":
            from mastapy.gears.fe_model.conical import _1216

            return self._parent._cast(_1216.ConicalSetFEModel)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1238.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1238

            return self._parent._cast(_1238.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1239.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1239

            return self._parent._cast(_1239.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1240.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1240

            return self._parent._cast(_1240.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_detail(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "_1241.GearSetImplementationDetail":
            from mastapy.gears.analysis import _1241

            return self._parent._cast(_1241.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis",
        ) -> "GearSetDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearSetDesignAnalysis._Cast_GearSetDesignAnalysis":
        return self._Cast_GearSetDesignAnalysis(self)
