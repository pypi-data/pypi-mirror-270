"""CVTAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CVTAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2605
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7400,
        _7296,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTAdvancedSystemDeflection")


class CVTAdvancedSystemDeflection(_7309.BeltDriveAdvancedSystemDeflection):
    """CVTAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTAdvancedSystemDeflection")

    class _Cast_CVTAdvancedSystemDeflection:
        """Special nested class for casting CVTAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
            parent: "CVTAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_drive_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7309.BeltDriveAdvancedSystemDeflection":
            return self._parent._cast(_7309.BeltDriveAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7400.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7400,
            )

            return self._parent._cast(_7400.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7296.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7296,
            )

            return self._parent._cast(_7296.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_advanced_system_deflection(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
        ) -> "CVTAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTAdvancedSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2605.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTAdvancedSystemDeflection._Cast_CVTAdvancedSystemDeflection":
        return self._Cast_CVTAdvancedSystemDeflection(self)
