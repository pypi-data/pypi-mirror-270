"""GearSetImplementationAnalysisAbstract"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1236
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysisAbstract"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _627, _628
    from mastapy.gears.manufacturing.bevel import _797
    from mastapy.gears.ltca import _853
    from mastapy.gears.ltca.cylindrical import _867, _869
    from mastapy.gears.ltca.conical import _875
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118
    from mastapy.gears.analysis import _1238, _1240, _1227


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysisAbstract",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysisAbstract")


class GearSetImplementationAnalysisAbstract(_1236.GearSetDesignAnalysis):
    """GearSetImplementationAnalysisAbstract

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS_ABSTRACT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetImplementationAnalysisAbstract"
    )

    class _Cast_GearSetImplementationAnalysisAbstract:
        """Special nested class for casting GearSetImplementationAnalysisAbstract to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
            parent: "GearSetImplementationAnalysisAbstract",
        ):
            self._parent = parent

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1236.GearSetDesignAnalysis":
            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_627.CylindricalManufacturedGearSetDutyCycle":
            from mastapy.gears.manufacturing.cylindrical import _627

            return self._parent._cast(_627.CylindricalManufacturedGearSetDutyCycle)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_628.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_797.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_853.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _853

            return self._parent._cast(_853.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_867.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _867

            return self._parent._cast(_867.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_869.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _869

            return self._parent._cast(_869.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_875.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalGearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_micro_geometry_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1118.CylindricalGearSetMicroGeometryDutyCycle":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118

            return self._parent._cast(_1118.CylindricalGearSetMicroGeometryDutyCycle)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1238.GearSetImplementationAnalysis":
            from mastapy.gears.analysis import _1238

            return self._parent._cast(_1238.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_duty_cycle(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "_1240.GearSetImplementationAnalysisDutyCycle":
            from mastapy.gears.analysis import _1240

            return self._parent._cast(_1240.GearSetImplementationAnalysisDutyCycle)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
        ) -> "GearSetImplementationAnalysisAbstract":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "GearSetImplementationAnalysisAbstract.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysisAbstract._Cast_GearSetImplementationAnalysisAbstract":
        return self._Cast_GearSetImplementationAnalysisAbstract(self)
