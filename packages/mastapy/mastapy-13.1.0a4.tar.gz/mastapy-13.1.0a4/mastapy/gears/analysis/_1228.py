"""GearDesignAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1225
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearDesignAnalysis"
)

if TYPE_CHECKING:
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
    from mastapy.gears.analysis import _1229, _1230, _1231


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignAnalysis",)


Self = TypeVar("Self", bound="GearDesignAnalysis")


class GearDesignAnalysis(_1225.AbstractGearAnalysis):
    """GearDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignAnalysis")

    class _Cast_GearDesignAnalysis:
        """Special nested class for casting GearDesignAnalysis to subclasses."""

        def __init__(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
            parent: "GearDesignAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_gear_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1225.AbstractGearAnalysis":
            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_619.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalGearManufacturingConfig)

        @property
        def cylindrical_manufactured_gear_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_623.CylindricalManufacturedGearDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _623

            return self._parent._cast(_623.CylindricalManufacturedGearDutyCycle)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_624.CylindricalManufacturedGearLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _624

            return self._parent._cast(_624.CylindricalManufacturedGearLoadCase)

        @property
        def conical_gear_manufacturing_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_782.ConicalGearManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _782

            return self._parent._cast(_782.ConicalGearManufacturingAnalysis)

        @property
        def conical_gear_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_783.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_784.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_795.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_796.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_801.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _801

            return self._parent._cast(_801.ConicalWheelManufacturingConfig)

        @property
        def gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_847.GearLoadDistributionAnalysis":
            from mastapy.gears.ltca import _847

            return self._parent._cast(_847.GearLoadDistributionAnalysis)

        @property
        def cylindrical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_863.CylindricalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _863

            return self._parent._cast(_863.CylindricalGearLoadDistributionAnalysis)

        @property
        def conical_gear_load_distribution_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_874.ConicalGearLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _874

            return self._parent._cast(_874.ConicalGearLoadDistributionAnalysis)

        @property
        def gear_load_case_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_880.GearLoadCaseBase":
            from mastapy.gears.load_case import _880

            return self._parent._cast(_880.GearLoadCaseBase)

        @property
        def worm_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_883.WormGearLoadCase":
            from mastapy.gears.load_case.worm import _883

            return self._parent._cast(_883.WormGearLoadCase)

        @property
        def face_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_886.FaceGearLoadCase":
            from mastapy.gears.load_case.face import _886

            return self._parent._cast(_886.FaceGearLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_889.CylindricalGearLoadCase":
            from mastapy.gears.load_case.cylindrical import _889

            return self._parent._cast(_889.CylindricalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_892.ConicalGearLoadCase":
            from mastapy.gears.load_case.conical import _892

            return self._parent._cast(_892.ConicalGearLoadCase)

        @property
        def concept_gear_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_895.ConceptGearLoadCase":
            from mastapy.gears.load_case.concept import _895

            return self._parent._cast(_895.ConceptGearLoadCase)

        @property
        def bevel_load_case(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_898.BevelLoadCase":
            from mastapy.gears.load_case.bevel import _898

            return self._parent._cast(_898.BevelLoadCase)

        @property
        def cylindrical_gear_tiff_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_905.CylindricalGearTIFFAnalysis":
            from mastapy.gears.gear_two_d_fe_analysis import _905

            return self._parent._cast(_905.CylindricalGearTIFFAnalysis)

        @property
        def cylindrical_gear_tiff_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_906.CylindricalGearTIFFAnalysisDutyCycle":
            from mastapy.gears.gear_two_d_fe_analysis import _906

            return self._parent._cast(_906.CylindricalGearTIFFAnalysisDutyCycle)

        @property
        def face_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1001.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1110.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1111.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111

            return self._parent._cast(_1111.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1112.CylindricalGearMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1112

            return self._parent._cast(_1112.CylindricalGearMicroGeometryDutyCycle)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1114.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1207.GearFEModel":
            from mastapy.gears.fe_model import _1207

            return self._parent._cast(_1207.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1211.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1211

            return self._parent._cast(_1211.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1214.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1214

            return self._parent._cast(_1214.ConicalGearFEModel)

        @property
        def gear_implementation_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1229.GearImplementationAnalysis":
            from mastapy.gears.analysis import _1229

            return self._parent._cast(_1229.GearImplementationAnalysis)

        @property
        def gear_implementation_analysis_duty_cycle(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1230.GearImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1230

            return self._parent._cast(_1230.GearImplementationAnalysisDutyCycle)

        @property
        def gear_implementation_detail(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "_1231.GearImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "GearDesignAnalysis._Cast_GearDesignAnalysis",
        ) -> "GearDesignAnalysis":
            return self._parent

        def __getattr__(self: "GearDesignAnalysis._Cast_GearDesignAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "GearDesignAnalysis._Cast_GearDesignAnalysis":
        return self._Cast_GearDesignAnalysis(self)
