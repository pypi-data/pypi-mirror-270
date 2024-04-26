"""BevelDifferentialGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7450,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2534
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7312,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7443,
        _7444,
        _7438,
        _7466,
        _7492,
        _7530,
        _7432,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetCompoundAdvancedSystemDeflection")


class BevelDifferentialGearSetCompoundAdvancedSystemDeflection(
    _7450.BevelGearSetCompoundAdvancedSystemDeflection
):
    """BevelDifferentialGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
            parent: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7450.BevelGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7450.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7438.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7438,
            )

            return self._parent._cast(
                _7438.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7466.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(
                _7466.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7492.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(_7492.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7432.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
        ) -> "BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection",
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
        self: Self,
        instance_to_wrap: "BevelDifferentialGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2534.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

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
    ) -> "List[_7312.BevelDifferentialGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearSetAdvancedSystemDeflection]

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
    def bevel_differential_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7443.BevelDifferentialGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7444.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7312.BevelDifferentialGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearSetAdvancedSystemDeflection]

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
    ) -> "BevelDifferentialGearSetCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialGearSetCompoundAdvancedSystemDeflection(self)
