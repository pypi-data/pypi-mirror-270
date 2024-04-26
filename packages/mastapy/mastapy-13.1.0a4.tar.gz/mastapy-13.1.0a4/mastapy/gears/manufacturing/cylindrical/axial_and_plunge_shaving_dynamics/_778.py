"""ShavingDynamicsViewModelBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _635
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ShavingDynamicsViewModelBase",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _761,
        _767,
        _777,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ShavingDynamicsViewModelBase",)


Self = TypeVar("Self", bound="ShavingDynamicsViewModelBase")


class ShavingDynamicsViewModelBase(_635.GearManufacturingConfigurationViewModel):
    """ShavingDynamicsViewModelBase

    This is a mastapy class.
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShavingDynamicsViewModelBase")

    class _Cast_ShavingDynamicsViewModelBase:
        """Special nested class for casting ShavingDynamicsViewModelBase to subclasses."""

        def __init__(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
            parent: "ShavingDynamicsViewModelBase",
        ):
            self._parent = parent

        @property
        def gear_manufacturing_configuration_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_635.GearManufacturingConfigurationViewModel":
            return self._parent._cast(_635.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_761.ConventionalShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _761,
            )

            return self._parent._cast(_761.ConventionalShavingDynamicsViewModel)

        @property
        def plunge_shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_767.PlungeShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _767,
            )

            return self._parent._cast(_767.PlungeShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "_777.ShavingDynamicsViewModel":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _777,
            )

            return self._parent._cast(_777.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
        ) -> "ShavingDynamicsViewModelBase":
            return self._parent

        def __getattr__(
            self: "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShavingDynamicsViewModelBase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ShavingDynamicsViewModelBase._Cast_ShavingDynamicsViewModelBase":
        return self._Cast_ShavingDynamicsViewModelBase(self)
