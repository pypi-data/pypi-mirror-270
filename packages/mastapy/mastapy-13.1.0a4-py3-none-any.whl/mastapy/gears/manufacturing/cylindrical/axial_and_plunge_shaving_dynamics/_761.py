"""ConventionalShavingDynamicsViewModel"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _777,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics",
    "ConventionalShavingDynamicsViewModel",
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
        _778,
    )
    from mastapy.gears.manufacturing.cylindrical import _635


__docformat__ = "restructuredtext en"
__all__ = ("ConventionalShavingDynamicsViewModel",)


Self = TypeVar("Self", bound="ConventionalShavingDynamicsViewModel")


class ConventionalShavingDynamicsViewModel(
    _777.ShavingDynamicsViewModel["_758.ConventionalShavingDynamics"]
):
    """ConventionalShavingDynamicsViewModel

    This is a mastapy class.
    """

    TYPE = _CONVENTIONAL_SHAVING_DYNAMICS_VIEW_MODEL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConventionalShavingDynamicsViewModel")

    class _Cast_ConventionalShavingDynamicsViewModel:
        """Special nested class for casting ConventionalShavingDynamicsViewModel to subclasses."""

        def __init__(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
            parent: "ConventionalShavingDynamicsViewModel",
        ):
            self._parent = parent

        @property
        def shaving_dynamics_view_model(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
        ) -> "_777.ShavingDynamicsViewModel":
            return self._parent._cast(_777.ShavingDynamicsViewModel)

        @property
        def shaving_dynamics_view_model_base(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
        ) -> "_778.ShavingDynamicsViewModelBase":
            from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
                _778,
            )

            return self._parent._cast(_778.ShavingDynamicsViewModelBase)

        @property
        def gear_manufacturing_configuration_view_model(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
        ) -> "_635.GearManufacturingConfigurationViewModel":
            from mastapy.gears.manufacturing.cylindrical import _635

            return self._parent._cast(_635.GearManufacturingConfigurationViewModel)

        @property
        def conventional_shaving_dynamics_view_model(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
        ) -> "ConventionalShavingDynamicsViewModel":
            return self._parent

        def __getattr__(
            self: "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel",
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
        self: Self, instance_to_wrap: "ConventionalShavingDynamicsViewModel.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConventionalShavingDynamicsViewModel._Cast_ConventionalShavingDynamicsViewModel":
        return self._Cast_ConventionalShavingDynamicsViewModel(self)
