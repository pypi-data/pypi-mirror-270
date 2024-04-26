"""FaceGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7492,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "FaceGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7356,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7485,
        _7486,
        _7530,
        _7432,
        _7511,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="FaceGearSetCompoundAdvancedSystemDeflection")


class FaceGearSetCompoundAdvancedSystemDeflection(
    _7492.GearSetCompoundAdvancedSystemDeflection
):
    """FaceGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearSetCompoundAdvancedSystemDeflection"
    )

    class _Cast_FaceGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting FaceGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
            parent: "FaceGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7492.GearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7492.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7432.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7432,
            )

            return self._parent._cast(
                _7432.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7511.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7511,
            )

            return self._parent._cast(_7511.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
        ) -> "FaceGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "FaceGearSetCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2547.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

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
    ) -> "List[_7356.FaceGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearSetAdvancedSystemDeflection]

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
    def face_gears_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7485.FaceGearCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_compound_advanced_system_deflection(
        self: Self,
    ) -> "List[_7486.FaceGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.FaceGearMeshCompoundAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesCompoundAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7356.FaceGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.FaceGearSetAdvancedSystemDeflection]

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
    ) -> "FaceGearSetCompoundAdvancedSystemDeflection._Cast_FaceGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_FaceGearSetCompoundAdvancedSystemDeflection(self)
