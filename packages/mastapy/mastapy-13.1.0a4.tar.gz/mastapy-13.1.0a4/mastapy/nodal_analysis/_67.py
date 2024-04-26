"""FEStiffnessNode"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_STIFFNESS_NODE = python_net_import("SMT.MastaAPI.NodalAnalysis", "FEStiffnessNode")

if TYPE_CHECKING:
    from mastapy.gears.ltca import _841, _843, _855
    from mastapy.gears.ltca.cylindrical import _859, _861
    from mastapy.gears.ltca.conical import _871, _873
    from mastapy.system_model.fe import _2403


__docformat__ = "restructuredtext en"
__all__ = ("FEStiffnessNode",)


Self = TypeVar("Self", bound="FEStiffnessNode")


class FEStiffnessNode(_0.APIBase):
    """FEStiffnessNode

    This is a mastapy class.
    """

    TYPE = _FE_STIFFNESS_NODE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEStiffnessNode")

    class _Cast_FEStiffnessNode:
        """Special nested class for casting FEStiffnessNode to subclasses."""

        def __init__(
            self: "FEStiffnessNode._Cast_FEStiffnessNode", parent: "FEStiffnessNode"
        ):
            self._parent = parent

        @property
        def gear_bending_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_841.GearBendingStiffnessNode":
            from mastapy.gears.ltca import _841

            return self._parent._cast(_841.GearBendingStiffnessNode)

        @property
        def gear_contact_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_843.GearContactStiffnessNode":
            from mastapy.gears.ltca import _843

            return self._parent._cast(_843.GearContactStiffnessNode)

        @property
        def gear_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_855.GearStiffnessNode":
            from mastapy.gears.ltca import _855

            return self._parent._cast(_855.GearStiffnessNode)

        @property
        def cylindrical_gear_bending_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_859.CylindricalGearBendingStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _859

            return self._parent._cast(_859.CylindricalGearBendingStiffnessNode)

        @property
        def cylindrical_gear_contact_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_861.CylindricalGearContactStiffnessNode":
            from mastapy.gears.ltca.cylindrical import _861

            return self._parent._cast(_861.CylindricalGearContactStiffnessNode)

        @property
        def conical_gear_bending_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_871.ConicalGearBendingStiffnessNode":
            from mastapy.gears.ltca.conical import _871

            return self._parent._cast(_871.ConicalGearBendingStiffnessNode)

        @property
        def conical_gear_contact_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_873.ConicalGearContactStiffnessNode":
            from mastapy.gears.ltca.conical import _873

            return self._parent._cast(_873.ConicalGearContactStiffnessNode)

        @property
        def fe_substructure_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "_2403.FESubstructureNode":
            from mastapy.system_model.fe import _2403

            return self._parent._cast(_2403.FESubstructureNode)

        @property
        def fe_stiffness_node(
            self: "FEStiffnessNode._Cast_FEStiffnessNode",
        ) -> "FEStiffnessNode":
            return self._parent

        def __getattr__(self: "FEStiffnessNode._Cast_FEStiffnessNode", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEStiffnessNode.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_degrees_of_freedom(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfDegreesOfFreedom

        if temp is None:
            return 0

        return temp

    @property
    def position_in_local_coordinate_system(self: Self) -> "Vector3D":
        """Vector3D"""
        temp = self.wrapped.PositionInLocalCoordinateSystem

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @position_in_local_coordinate_system.setter
    @enforce_parameter_types
    def position_in_local_coordinate_system(self: Self, value: "Vector3D"):
        value = conversion.mp_to_pn_vector3d(value)
        self.wrapped.PositionInLocalCoordinateSystem = value

    @property
    def node_index(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeIndex

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "FEStiffnessNode._Cast_FEStiffnessNode":
        return self._Cast_FEStiffnessNode(self)
