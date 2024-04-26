"""ConicalPinionManufacturingConfig"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _783
from mastapy._internal.cast_exception import CastException

_DATABASE_WITH_SELECTED_ITEM = python_net_import(
    "SMT.MastaAPI.UtilityGUI.Databases", "DatabaseWithSelectedItem"
)
_CONICAL_PINION_MANUFACTURING_CONFIG = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalPinionManufacturingConfig"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.bevel import _792, _788, _813, _817, _785
    from mastapy.gears.manufacturing.bevel.cutters import _820, _821
    from mastapy.gears.analysis import _1231, _1228, _1225


__docformat__ = "restructuredtext en"
__all__ = ("ConicalPinionManufacturingConfig",)


Self = TypeVar("Self", bound="ConicalPinionManufacturingConfig")


class ConicalPinionManufacturingConfig(_783.ConicalGearManufacturingConfig):
    """ConicalPinionManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MANUFACTURING_CONFIG
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalPinionManufacturingConfig")

    class _Cast_ConicalPinionManufacturingConfig:
        """Special nested class for casting ConicalPinionManufacturingConfig to subclasses."""

        def __init__(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
            parent: "ConicalPinionManufacturingConfig",
        ):
            self._parent = parent

        @property
        def conical_gear_manufacturing_config(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "_783.ConicalGearManufacturingConfig":
            return self._parent._cast(_783.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def gear_implementation_detail(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "_1231.GearImplementationDetail":
            from mastapy.gears.analysis import _1231

            return self._parent._cast(_1231.GearImplementationDetail)

        @property
        def gear_design_analysis(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "_1228.GearDesignAnalysis":
            from mastapy.gears.analysis import _1228

            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def conical_pinion_manufacturing_config(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
        ) -> "ConicalPinionManufacturingConfig":
            return self._parent

        def __getattr__(
            self: "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalPinionManufacturingConfig.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_finish_manufacturing_machine(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PinionFinishManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @pinion_finish_manufacturing_machine.setter
    @enforce_parameter_types
    def pinion_finish_manufacturing_machine(self: Self, value: "str"):
        self.wrapped.PinionFinishManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def pinion_rough_manufacturing_machine(self: Self) -> "str":
        """str"""
        temp = self.wrapped.PinionRoughManufacturingMachine.SelectedItemName

        if temp is None:
            return ""

        return temp

    @pinion_rough_manufacturing_machine.setter
    @enforce_parameter_types
    def pinion_rough_manufacturing_machine(self: Self, value: "str"):
        self.wrapped.PinionRoughManufacturingMachine.SetSelectedItem(
            str(value) if value is not None else ""
        )

    @property
    def mesh_config(self: Self) -> "_792.ConicalMeshManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalMeshManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeshConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_concave_ob_configuration(
        self: Self,
    ) -> "_788.ConicalMeshFlankManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalMeshFlankManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConcaveOBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_convex_ib_configuration(
        self: Self,
    ) -> "_788.ConicalMeshFlankManufacturingConfig":
        """mastapy.gears.manufacturing.bevel.ConicalMeshFlankManufacturingConfig

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionConvexIBConfiguration

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_cutter_parameters_concave(
        self: Self,
    ) -> "_813.PinionFinishMachineSettings":
        """mastapy.gears.manufacturing.bevel.PinionFinishMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionCutterParametersConcave

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_cutter_parameters_convex(
        self: Self,
    ) -> "_813.PinionFinishMachineSettings":
        """mastapy.gears.manufacturing.bevel.PinionFinishMachineSettings

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionCutterParametersConvex

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_finish_cutter(self: Self) -> "_820.PinionFinishCutter":
        """mastapy.gears.manufacturing.bevel.cutters.PinionFinishCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionFinishCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_rough_cutter(self: Self) -> "_821.PinionRoughCutter":
        """mastapy.gears.manufacturing.bevel.cutters.PinionRoughCutter

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRoughCutter

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def pinion_rough_machine_setting(self: Self) -> "_817.PinionRoughMachineSetting":
        """mastapy.gears.manufacturing.bevel.PinionRoughMachineSetting

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PinionRoughMachineSetting

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalPinionManufacturingConfig._Cast_ConicalPinionManufacturingConfig":
        return self._Cast_ConicalPinionManufacturingConfig(self)
