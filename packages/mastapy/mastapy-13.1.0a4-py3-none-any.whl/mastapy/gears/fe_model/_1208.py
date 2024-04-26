"""GearMeshFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.analysis import _1235
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearMeshFEModel")

if TYPE_CHECKING:
    from mastapy.gears.fe_model.cylindrical import _1212
    from mastapy.gears.fe_model.conical import _1215
    from mastapy.gears.analysis import _1232, _1226


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshFEModel",)


Self = TypeVar("Self", bound="GearMeshFEModel")


class GearMeshFEModel(_1235.GearMeshImplementationDetail):
    """GearMeshFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshFEModel")

    class _Cast_GearMeshFEModel:
        """Special nested class for casting GearMeshFEModel to subclasses."""

        def __init__(
            self: "GearMeshFEModel._Cast_GearMeshFEModel", parent: "GearMeshFEModel"
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "_1235.GearMeshImplementationDetail":
            return self._parent._cast(_1235.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "_1232.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1232

            return self._parent._cast(_1232.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "_1226.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1226

            return self._parent._cast(_1226.AbstractGearMeshAnalysis)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "_1212.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1212

            return self._parent._cast(_1212.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "_1215.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1215

            return self._parent._cast(_1215.ConicalMeshFEModel)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshFEModel._Cast_GearMeshFEModel",
        ) -> "GearMeshFEModel":
            return self._parent

        def __getattr__(self: "GearMeshFEModel._Cast_GearMeshFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_loads_per_contact(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfLoadsPerContact

        if temp is None:
            return 0

        return temp

    @number_of_loads_per_contact.setter
    @enforce_parameter_types
    def number_of_loads_per_contact(self: Self, value: "int"):
        self.wrapped.NumberOfLoadsPerContact = int(value) if value is not None else 0

    @property
    def number_of_rotations(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfRotations

        if temp is None:
            return 0

        return temp

    @number_of_rotations.setter
    @enforce_parameter_types
    def number_of_rotations(self: Self, value: "int"):
        self.wrapped.NumberOfRotations = int(value) if value is not None else 0

    @property
    def cast_to(self: Self) -> "GearMeshFEModel._Cast_GearMeshFEModel":
        return self._Cast_GearMeshFEModel(self)
