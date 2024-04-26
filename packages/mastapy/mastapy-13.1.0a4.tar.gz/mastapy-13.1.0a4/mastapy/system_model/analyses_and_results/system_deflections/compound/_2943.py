"""KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2792
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2946,
        _2949,
        _2935,
        _2974,
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection(
    _2908.ConicalGearSetCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2908.ConicalGearSetCompoundSystemDeflection":
            return self._parent._cast(_2908.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2935.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2946.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(
                _2946.KlingelnbergCycloPalloidHypoidGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "_2949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(
                _2949.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_2792.KlingelnbergCycloPalloidConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidConicalGearSetSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetCompoundSystemDeflection(
                self
            )
        )
