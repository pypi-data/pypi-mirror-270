"""BoltedJointSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2829
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BoltedJointSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6857
    from mastapy.system_model.analyses_and_results.power_flows import _4074
    from mastapy.system_model.analyses_and_results.system_deflections import (
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
__all__ = ("BoltedJointSystemDeflection",)


Self = TypeVar("Self", bound="BoltedJointSystemDeflection")


class BoltedJointSystemDeflection(_2829.SpecialisedAssemblySystemDeflection):
    """BoltedJointSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointSystemDeflection")

    class _Cast_BoltedJointSystemDeflection:
        """Special nested class for casting BoltedJointSystemDeflection to subclasses."""

        def __init__(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
            parent: "BoltedJointSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_system_deflection(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2829.SpecialisedAssemblySystemDeflection":
            return self._parent._cast(_2829.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2708.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2708,
            )

            return self._parent._cast(_2708.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2808.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_7573.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7573

            return self._parent._cast(_7573.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolted_joint_system_deflection(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
        ) -> "BoltedJointSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2461.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6857.BoltedJointLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BoltedJointLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4074.BoltedJointPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BoltedJointPowerFlow

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
    ) -> "BoltedJointSystemDeflection._Cast_BoltedJointSystemDeflection":
        return self._Cast_BoltedJointSystemDeflection(self)
