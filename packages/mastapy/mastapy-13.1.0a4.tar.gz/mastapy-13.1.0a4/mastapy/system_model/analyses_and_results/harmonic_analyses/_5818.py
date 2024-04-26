"""PeriodicExcitationWithReferenceShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5705
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PeriodicExcitationWithReferenceShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5759,
        _5760,
        _5761,
        _5762,
        _5763,
        _5764,
        _5765,
        _5766,
        _5767,
        _5768,
        _5769,
        _5770,
        _5785,
        _5835,
        _5861,
    )


__docformat__ = "restructuredtext en"
__all__ = ("PeriodicExcitationWithReferenceShaft",)


Self = TypeVar("Self", bound="PeriodicExcitationWithReferenceShaft")


class PeriodicExcitationWithReferenceShaft(_5705.AbstractPeriodicExcitationDetail):
    """PeriodicExcitationWithReferenceShaft

    This is a mastapy class.
    """

    TYPE = _PERIODIC_EXCITATION_WITH_REFERENCE_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PeriodicExcitationWithReferenceShaft")

    class _Cast_PeriodicExcitationWithReferenceShaft:
        """Special nested class for casting PeriodicExcitationWithReferenceShaft to subclasses."""

        def __init__(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
            parent: "PeriodicExcitationWithReferenceShaft",
        ):
            self._parent = parent

        @property
        def abstract_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5705.AbstractPeriodicExcitationDetail":
            return self._parent._cast(_5705.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5759.ElectricMachinePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5759,
            )

            return self._parent._cast(_5759.ElectricMachinePeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5760.ElectricMachineRotorXForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(
                _5760.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5761.ElectricMachineRotorXMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(
                _5761.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5762.ElectricMachineRotorYForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(
                _5762.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5763.ElectricMachineRotorYMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5763,
            )

            return self._parent._cast(
                _5763.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5764.ElectricMachineRotorZForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5764,
            )

            return self._parent._cast(
                _5764.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5765.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5765,
            )

            return self._parent._cast(
                _5765.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5766.ElectricMachineStatorToothLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5766,
            )

            return self._parent._cast(
                _5766.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5767.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5767,
            )

            return self._parent._cast(
                _5767.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5768.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5768,
            )

            return self._parent._cast(
                _5768.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5769.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5769,
            )

            return self._parent._cast(
                _5769.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5770.ElectricMachineTorqueRipplePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5770,
            )

            return self._parent._cast(
                _5770.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def general_periodic_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5785.GeneralPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(_5785.GeneralPeriodicExcitationDetail)

        @property
        def single_node_periodic_excitation_with_reference_shaft(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5835.SingleNodePeriodicExcitationWithReferenceShaft":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(
                _5835.SingleNodePeriodicExcitationWithReferenceShaft
            )

        @property
        def unbalanced_mass_excitation_detail(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "_5861.UnbalancedMassExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5861,
            )

            return self._parent._cast(_5861.UnbalancedMassExcitationDetail)

        @property
        def periodic_excitation_with_reference_shaft(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
        ) -> "PeriodicExcitationWithReferenceShaft":
            return self._parent

        def __getattr__(
            self: "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft",
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
        self: Self, instance_to_wrap: "PeriodicExcitationWithReferenceShaft.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "PeriodicExcitationWithReferenceShaft._Cast_PeriodicExcitationWithReferenceShaft":
        return self._Cast_PeriodicExcitationWithReferenceShaft(self)
