"""GearMeshImplementationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1232
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _626
    from mastapy.gears.manufacturing.bevel import _791
    from mastapy.gears.ltca import _848
    from mastapy.gears.ltca.cylindrical import _864
    from mastapy.gears.ltca.conical import _877
    from mastapy.gears.analysis import _1226


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationAnalysis",)


Self = TypeVar("Self", bound="GearMeshImplementationAnalysis")


class GearMeshImplementationAnalysis(_1232.GearMeshDesignAnalysis):
    """GearMeshImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshImplementationAnalysis")

    class _Cast_GearMeshImplementationAnalysis:
        """Special nested class for casting GearMeshImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
            parent: "GearMeshImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_1232.GearMeshDesignAnalysis":
            return self._parent._cast(_1232.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def cylindrical_manufactured_gear_mesh_load_case(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_626.CylindricalManufacturedGearMeshLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalManufacturedGearMeshLoadCase)

        @property
        def conical_mesh_manufacturing_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_791.ConicalMeshManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _791

            return self._parent._cast(_791.ConicalMeshManufacturingAnalysis)

        @property
        def gear_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_848.GearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca import _848

            return self._parent._cast(_848.GearMeshLoadDistributionAnalysis)

        @property
        def cylindrical_gear_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_864.CylindricalGearMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _864

            return self._parent._cast(_864.CylindricalGearMeshLoadDistributionAnalysis)

        @property
        def conical_mesh_load_distribution_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "_877.ConicalMeshLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _877

            return self._parent._cast(_877.ConicalMeshLoadDistributionAnalysis)

        @property
        def gear_mesh_implementation_analysis(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
        ) -> "GearMeshImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationAnalysis._Cast_GearMeshImplementationAnalysis":
        return self._Cast_GearMeshImplementationAnalysis(self)
