"""GearImplementationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1228
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1754
    from mastapy.gears.manufacturing.cylindrical import _619
    from mastapy.gears.manufacturing.bevel import _783, _784, _785, _795, _796, _801
    from mastapy.gears.gear_designs.face import _1001
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
        _1110,
        _1111,
        _1114,
    )
    from mastapy.gears.fe_model import _1207
    from mastapy.gears.fe_model.cylindrical import _1211
    from mastapy.gears.fe_model.conical import _1214
    from mastapy.gears.analysis import _1225


__docformat__ = "restructuredtext en"
__all__ = ("GearImplementationDetail",)


Self = TypeVar("Self", bound="GearImplementationDetail")


class GearImplementationDetail(_1228.GearDesignAnalysis):
    """GearImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearImplementationDetail")

    class _Cast_GearImplementationDetail:
        """Special nested class for casting GearImplementationDetail to subclasses."""

        def __init__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
            parent: "GearImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_design_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1228.GearDesignAnalysis":
            return self._parent._cast(_1228.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1225.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1225

            return self._parent._cast(_1225.AbstractGearAnalysis)

        @property
        def cylindrical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_619.CylindricalGearManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _619

            return self._parent._cast(_619.CylindricalGearManufacturingConfig)

        @property
        def conical_gear_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_783.ConicalGearManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _783

            return self._parent._cast(_783.ConicalGearManufacturingConfig)

        @property
        def conical_gear_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_784.ConicalGearMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _784

            return self._parent._cast(_784.ConicalGearMicroGeometryConfig)

        @property
        def conical_gear_micro_geometry_config_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_785.ConicalGearMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalGearMicroGeometryConfigBase)

        @property
        def conical_pinion_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_795.ConicalPinionManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _795

            return self._parent._cast(_795.ConicalPinionManufacturingConfig)

        @property
        def conical_pinion_micro_geometry_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_796.ConicalPinionMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _796

            return self._parent._cast(_796.ConicalPinionMicroGeometryConfig)

        @property
        def conical_wheel_manufacturing_config(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_801.ConicalWheelManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _801

            return self._parent._cast(_801.ConicalWheelManufacturingConfig)

        @property
        def face_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1001.FaceGearMicroGeometry":
            from mastapy.gears.gear_designs.face import _1001

            return self._parent._cast(_1001.FaceGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1110.CylindricalGearMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1110

            return self._parent._cast(_1110.CylindricalGearMicroGeometry)

        @property
        def cylindrical_gear_micro_geometry_base(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1111.CylindricalGearMicroGeometryBase":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1111

            return self._parent._cast(_1111.CylindricalGearMicroGeometryBase)

        @property
        def cylindrical_gear_micro_geometry_per_tooth(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1114.CylindricalGearMicroGeometryPerTooth":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1114

            return self._parent._cast(_1114.CylindricalGearMicroGeometryPerTooth)

        @property
        def gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1207.GearFEModel":
            from mastapy.gears.fe_model import _1207

            return self._parent._cast(_1207.GearFEModel)

        @property
        def cylindrical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1211.CylindricalGearFEModel":
            from mastapy.gears.fe_model.cylindrical import _1211

            return self._parent._cast(_1211.CylindricalGearFEModel)

        @property
        def conical_gear_fe_model(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "_1214.ConicalGearFEModel":
            from mastapy.gears.fe_model.conical import _1214

            return self._parent._cast(_1214.ConicalGearFEModel)

        @property
        def gear_implementation_detail(
            self: "GearImplementationDetail._Cast_GearImplementationDetail",
        ) -> "GearImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearImplementationDetail._Cast_GearImplementationDetail", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def user_specified_data(self: Self) -> "_1754.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "GearImplementationDetail._Cast_GearImplementationDetail":
        return self._Cast_GearImplementationDetail(self)
