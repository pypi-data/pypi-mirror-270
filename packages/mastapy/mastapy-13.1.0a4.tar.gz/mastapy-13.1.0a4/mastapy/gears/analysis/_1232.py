"""GearMeshDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshDesignAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1228, _1236, _1233, _1234, _1235
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
__all__ = ("GearMeshDesignAnalysis",)


Self = TypeVar("Self", bound="GearMeshDesignAnalysis")


class GearMeshDesignAnalysis(_1226.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDesignAnalysis")

    class _Cast_GearMeshDesignAnalysis:
        """Special nested class for casting GearMeshDesignAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
            parent: "GearMeshDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1226.AbstractGearMeshAnalysis":
            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_625.CylindricalManufacturedGearMeshDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _625

            return self._parent._cast(_625.CylindricalManufacturedGearMeshDutyCycle)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_626.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalManufacturedGearMeshLoadCase)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_629.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _629

            return self._parent._cast(_629.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_791.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalMeshManufacturingAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_792.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _792

            return self._parent._cast(_792.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_793.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _793

            return self._parent._cast(_793.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_794.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _794

            return self._parent._cast(_794.ConicalMeshMicroGeometryConfigBase)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_848.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _848

            return self._parent._cast(_848.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_864.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _864

            return self._parent._cast(_864.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_877.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _877

            return self._parent._cast(_877.ConicalMeshLoadDistributionAnalysis)

        @property
        def mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_882.MeshLoadCase":
            from mastapy.gears.load_case import _882

            return self._parent._cast(_882.MeshLoadCase)

        @property
        def worm_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_885.WormMeshLoadCase":
            from mastapy.gears.load_case.worm import _885

            return self._parent._cast(_885.WormMeshLoadCase)

        @property
        def face_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_888.FaceMeshLoadCase":
            from mastapy.gears.load_case.face import _888

            return self._parent._cast(_888.FaceMeshLoadCase)

        @property
        def cylindrical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_891.CylindricalMeshLoadCase":
            from mastapy.gears.load_case.cylindrical import _891

            return self._parent._cast(_891.CylindricalMeshLoadCase)

        @property
        def conical_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_894.ConicalMeshLoadCase":
            from mastapy.gears.load_case.conical import _894

            return self._parent._cast(_894.ConicalMeshLoadCase)

        @property
        def concept_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_897.ConceptMeshLoadCase":
            from mastapy.gears.load_case.concept import _897

            return self._parent._cast(_897.ConceptMeshLoadCase)

        @property
        def bevel_mesh_load_case(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_899.BevelMeshLoadCase":
            from mastapy.gears.load_case.bevel import _899

            return self._parent._cast(_899.BevelMeshLoadCase)

        @property
        def cylindrical_gear_mesh_tiff_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_901.CylindricalGearMeshTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _901

            return self._parent._cast(_901.CylindricalGearMeshTIFFAnalysis)

        @property
        def cylindrical_gear_mesh_tiff_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_902.CylindricalGearMeshTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _902

            return self._parent._cast(_902.CylindricalGearMeshTIFFAnalysisDutyCycle)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1000.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _1000

            return self._parent._cast(_1000.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1108.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108

            return self._parent._cast(_1108.CylindricalGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1109.CylindricalGearMeshMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1109

            return self._parent._cast(_1109.CylindricalGearMeshMicroGeometryDutyCycle)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1208.GearMeshFEModel":
            from mastapy.gears.fe_model import _1208

            return self._parent._cast(_1208.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1212.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1212

            return self._parent._cast(_1212.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1215.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1215

            return self._parent._cast(_1215.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1233.GearMeshImplementationAnalysis":
            from mastapy.gears.analysis import _1233

            return self._parent._cast(_1233.GearMeshImplementationAnalysis)

        @property
        def gear_mesh_implementation_analysis_duty_cycle(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1234.GearMeshImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1234

            return self._parent._cast(_1234.GearMeshImplementationAnalysisDutyCycle)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "_1235.GearMeshImplementationDetail":
            from mastapy.gears.analysis import _1235

            return self._parent._cast(_1235.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis",
        ) -> "GearMeshDesignAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self: Self) -> "_1228.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearA

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_b(self: Self) -> "_1228.GearDesignAnalysis":
        """mastapy.gears.analysis.GearDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearB

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set(self: Self) -> "_1236.GearSetDesignAnalysis":
        """mastapy.gears.analysis.GearSetDesignAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSet

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDesignAnalysis._Cast_GearMeshDesignAnalysis":
        return self._Cast_GearMeshDesignAnalysis(self)
