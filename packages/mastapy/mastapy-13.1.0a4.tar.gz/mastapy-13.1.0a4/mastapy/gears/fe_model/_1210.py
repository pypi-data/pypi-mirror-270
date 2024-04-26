"""GearSetFEModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Optional, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.analysis import _1241
from mastapy._internal.cast_exception import CastException

_TASK_PROGRESS = python_net_import("SMT.MastaAPIUtility", "TaskProgress")
_GEAR_SET_FE_MODEL = python_net_import("SMT.MastaAPI.Gears.FEModel", "GearSetFEModel")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _58
    from mastapy.gears.fe_model import _1207, _1208
    from mastapy import _7585
    from mastapy.gears.fe_model.cylindrical import _1213
    from mastapy.gears.fe_model.conical import _1216
    from mastapy.gears.analysis import _1236, _1227


__docformat__ = "restructuredtext en"
__all__ = ("GearSetFEModel",)


Self = TypeVar("Self", bound="GearSetFEModel")


class GearSetFEModel(_1241.GearSetImplementationDetail):
    """GearSetFEModel

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_FE_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetFEModel")

    class _Cast_GearSetFEModel:
        """Special nested class for casting GearSetFEModel to subclasses."""

        def __init__(
            self: "GearSetFEModel._Cast_GearSetFEModel", parent: "GearSetFEModel"
        ):
            self._parent = parent

        @property
        def gear_set_implementation_detail(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "_1241.GearSetImplementationDetail":
            return self._parent._cast(_1241.GearSetImplementationDetail)

        @property
        def gear_set_design_analysis(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_fe_model(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "_1213.CylindricalGearSetFEModel":
            from mastapy.gears.fe_model.cylindrical import _1213

            return self._parent._cast(_1213.CylindricalGearSetFEModel)

        @property
        def conical_set_fe_model(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "_1216.ConicalSetFEModel":
            from mastapy.gears.fe_model.conical import _1216

            return self._parent._cast(_1216.ConicalSetFEModel)

        @property
        def gear_set_fe_model(
            self: "GearSetFEModel._Cast_GearSetFEModel",
        ) -> "GearSetFEModel":
            return self._parent

        def __getattr__(self: "GearSetFEModel._Cast_GearSetFEModel", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetFEModel.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def comment(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Comment

        if temp is None:
            return ""

        return temp

    @comment.setter
    @enforce_parameter_types
    def comment(self: Self, value: "str"):
        self.wrapped.Comment = str(value) if value is not None else ""

    @property
    def element_order(self: Self) -> "_58.ElementOrder":
        """mastapy.nodal_analysis.ElementOrder"""
        temp = self.wrapped.ElementOrder

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.nodal_analysis._58", "ElementOrder"
        )(value)

    @element_order.setter
    @enforce_parameter_types
    def element_order(self: Self, value: "_58.ElementOrder"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.NodalAnalysis.ElementOrder"
        )
        self.wrapped.ElementOrder = value

    @property
    def number_of_coupled_teeth_either_side(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfCoupledTeethEitherSide

        if temp is None:
            return 0

        return temp

    @number_of_coupled_teeth_either_side.setter
    @enforce_parameter_types
    def number_of_coupled_teeth_either_side(self: Self, value: "int"):
        self.wrapped.NumberOfCoupledTeethEitherSide = (
            int(value) if value is not None else 0
        )

    @property
    def use_out_of_core_solver(self: Self) -> "Optional[bool]":
        """Optional[bool]"""
        temp = self.wrapped.UseOutOfCoreSolver

        if temp is None:
            return None

        return temp

    @use_out_of_core_solver.setter
    @enforce_parameter_types
    def use_out_of_core_solver(self: Self, value: "Optional[bool]"):
        self.wrapped.UseOutOfCoreSolver = value

    @property
    def gear_fe_models(self: Self) -> "List[_1207.GearFEModel]":
        """List[mastapy.gears.fe_model.GearFEModel]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mesh_fe_models(self: Self) -> "List[_1208.GearMeshFEModel]":
        """List[mastapy.gears.fe_model.GearMeshFEModel]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshFEModels

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def is_ready_for_altca(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsReadyForALTCA

        if temp is None:
            return False

        return temp

    def generate_stiffness_from_fe(self: Self):
        """Method does not return."""
        self.wrapped.GenerateStiffnessFromFE()

    def generate_stress_influence_coefficients_from_fe(self: Self):
        """Method does not return."""
        self.wrapped.GenerateStressInfluenceCoefficientsFromFE()

    def calculate_stiffness_from_fe(self: Self):
        """Method does not return."""
        self.wrapped.CalculateStiffnessFromFE()

    @enforce_parameter_types
    def calculate_stiffness_from_fe_with_progress(
        self: Self, progress: "_7585.TaskProgress"
    ):
        """Method does not return.

        Args:
            progress (mastapy.TaskProgress)
        """
        self.wrapped.CalculateStiffnessFromFE.Overloads[_TASK_PROGRESS](
            progress.wrapped if progress else None
        )

    @property
    def cast_to(self: Self) -> "GearSetFEModel._Cast_GearSetFEModel":
        return self._Cast_GearSetFEModel(self)
