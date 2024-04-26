"""BeltDriveCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7530,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BeltDriveCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2594
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7309,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7473,
        _7432,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BeltDriveCompoundAdvancedSystemDeflection")


class BeltDriveCompoundAdvancedSystemDeflection(
    _7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection
):
    """BeltDriveCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltDriveCompoundAdvancedSystemDeflection"
    )

    class _Cast_BeltDriveCompoundAdvancedSystemDeflection:
        """Special nested class for casting BeltDriveCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
            parent: "BeltDriveCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7432.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "_7473.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7473,
            )

            return self._parent._cast(_7473.CVTCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
        ) -> "BeltDriveCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "BeltDriveCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2594.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7309.BeltDriveAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BeltDriveAdvancedSystemDeflection]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7309.BeltDriveAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BeltDriveAdvancedSystemDeflection]

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
    ) -> "BeltDriveCompoundAdvancedSystemDeflection._Cast_BeltDriveCompoundAdvancedSystemDeflection":
        return self._Cast_BeltDriveCompoundAdvancedSystemDeflection(self)
