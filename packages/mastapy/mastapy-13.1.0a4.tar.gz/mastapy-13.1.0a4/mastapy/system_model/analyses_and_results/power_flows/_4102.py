"""CylindricalGearGeometricEntityDrawStyle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.power_flows import _4146
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "CylindricalGearGeometricEntityDrawStyle",
)

if TYPE_CHECKING:
    from mastapy.geometry import _314, _315


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearGeometricEntityDrawStyle",)


Self = TypeVar("Self", bound="CylindricalGearGeometricEntityDrawStyle")


class CylindricalGearGeometricEntityDrawStyle(_4146.PowerFlowDrawStyle):
    """CylindricalGearGeometricEntityDrawStyle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_GEOMETRIC_ENTITY_DRAW_STYLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearGeometricEntityDrawStyle"
    )

    class _Cast_CylindricalGearGeometricEntityDrawStyle:
        """Special nested class for casting CylindricalGearGeometricEntityDrawStyle to subclasses."""

        def __init__(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
            parent: "CylindricalGearGeometricEntityDrawStyle",
        ):
            self._parent = parent

        @property
        def power_flow_draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_4146.PowerFlowDrawStyle":
            return self._parent._cast(_4146.PowerFlowDrawStyle)

        @property
        def draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_314.DrawStyle":
            from mastapy.geometry import _314

            return self._parent._cast(_314.DrawStyle)

        @property
        def draw_style_base(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "_315.DrawStyleBase":
            from mastapy.geometry import _315

            return self._parent._cast(_315.DrawStyleBase)

        @property
        def cylindrical_gear_geometric_entity_draw_style(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
        ) -> "CylindricalGearGeometricEntityDrawStyle":
            return self._parent

        def __getattr__(
            self: "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle",
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
        self: Self, instance_to_wrap: "CylindricalGearGeometricEntityDrawStyle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearGeometricEntityDrawStyle._Cast_CylindricalGearGeometricEntityDrawStyle":
        return self._Cast_CylindricalGearGeometricEntityDrawStyle(self)
