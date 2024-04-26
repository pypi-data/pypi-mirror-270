"""BoltedJointAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7400
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "BoltedJointAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2461
    from mastapy.system_model.analyses_and_results.static_loads import _6857
    from mastapy.system_model.analyses_and_results.system_deflections import _2732
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7296,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BoltedJointAdvancedSystemDeflection")


class BoltedJointAdvancedSystemDeflection(
    _7400.SpecialisedAssemblyAdvancedSystemDeflection
):
    """BoltedJointAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointAdvancedSystemDeflection")

    class _Cast_BoltedJointAdvancedSystemDeflection:
        """Special nested class for casting BoltedJointAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
            parent: "BoltedJointAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bolted_joint_advanced_system_deflection(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
        ) -> "BoltedJointAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BoltedJointAdvancedSystemDeflection.TYPE"
    ):
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
    def assembly_system_deflection_results(
        self: Self,
    ) -> "List[_2732.BoltedJointSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BoltedJointSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblySystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> (
        "BoltedJointAdvancedSystemDeflection._Cast_BoltedJointAdvancedSystemDeflection"
    ):
        return self._Cast_BoltedJointAdvancedSystemDeflection(self)
