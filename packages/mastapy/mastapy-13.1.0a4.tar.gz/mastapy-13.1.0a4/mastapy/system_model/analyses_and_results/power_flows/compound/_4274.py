"""PlanetaryGearSetCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "PlanetaryGearSetCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4142
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4250,
        _4288,
        _4190,
        _4269,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetCompoundPowerFlow",)


Self = TypeVar("Self", bound="PlanetaryGearSetCompoundPowerFlow")


class PlanetaryGearSetCompoundPowerFlow(_4239.CylindricalGearSetCompoundPowerFlow):
    """PlanetaryGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetaryGearSetCompoundPowerFlow")

    class _Cast_PlanetaryGearSetCompoundPowerFlow:
        """Special nested class for casting PlanetaryGearSetCompoundPowerFlow to subclasses."""

        def __init__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
            parent: "PlanetaryGearSetCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4239.CylindricalGearSetCompoundPowerFlow":
            return self._parent._cast(_4239.CylindricalGearSetCompoundPowerFlow)

        @property
        def gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4250.GearSetCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4250,
            )

            return self._parent._cast(_4250.GearSetCompoundPowerFlow)

        @property
        def specialised_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4288.SpecialisedAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.SpecialisedAssemblyCompoundPowerFlow)

        @property
        def abstract_assembly_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4190.AbstractAssemblyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4190,
            )

            return self._parent._cast(_4190.AbstractAssemblyCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_4269.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4269,
            )

            return self._parent._cast(_4269.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def planetary_gear_set_compound_power_flow(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
        ) -> "PlanetaryGearSetCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "PlanetaryGearSetCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4142.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4142.PlanetaryGearSetPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.PlanetaryGearSetPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PlanetaryGearSetCompoundPowerFlow._Cast_PlanetaryGearSetCompoundPowerFlow":
        return self._Cast_PlanetaryGearSetCompoundPowerFlow(self)
