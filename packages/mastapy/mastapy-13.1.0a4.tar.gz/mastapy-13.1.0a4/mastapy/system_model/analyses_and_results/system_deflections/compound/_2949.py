"""KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2559
    from mastapy.system_model.analyses_and_results.system_deflections import _2798
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2947,
        _2948,
        _2908,
        _2935,
        _2974,
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection(
    _2943.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2943.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            return self._parent._cast(
                _2943.KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection
            )

        @property
        def conical_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2908.ConicalGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2908,
            )

            return self._parent._cast(_2908.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2935.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(
        self: Self,
    ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(
        self: Self,
    ) -> "_2559.KlingelnbergCycloPalloidSpiralBevelGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGearSet

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
    ) -> "List[_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]

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
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_compound_system_deflection(
        self: Self,
    ) -> "List[_2947.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsCompoundSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_compound_system_deflection(
        self: Self,
    ) -> "List[_2948.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesCompoundSystemDeflection
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2798.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection(
            self
        )
