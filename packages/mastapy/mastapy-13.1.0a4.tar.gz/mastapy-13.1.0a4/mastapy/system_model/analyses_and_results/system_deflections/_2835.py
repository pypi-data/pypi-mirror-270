"""SpringDamperSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2754
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SpringDamperSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2623
    from mastapy.system_model.analyses_and_results.static_loads import _6985
    from mastapy.system_model.analyses_and_results.power_flows import _4164
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2829,
        _2708,
        _2808,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7573,
        _7574,
        _7571,
    )
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperSystemDeflection",)


Self = TypeVar("Self", bound="SpringDamperSystemDeflection")


class SpringDamperSystemDeflection(_2754.CouplingSystemDeflection):
    """SpringDamperSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperSystemDeflection")

    class _Cast_SpringDamperSystemDeflection:
        """Special nested class for casting SpringDamperSystemDeflection to subclasses."""

        def __init__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            parent: "SpringDamperSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2754.CouplingSystemDeflection":
            return self._parent._cast(_2754.CouplingSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2829,
            )

            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def spring_damper_system_deflection(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
        ) -> "SpringDamperSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2623.SpringDamper":
        """mastapy.system_model.part_model.couplings.SpringDamper

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6985.SpringDamperLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpringDamperLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4164.SpringDamperPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SpringDamperPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpringDamperSystemDeflection._Cast_SpringDamperSystemDeflection":
        return self._Cast_SpringDamperSystemDeflection(self)
