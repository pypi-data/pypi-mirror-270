"""AGMAGleasonConicalGearSetCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2908
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2713
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2887,
        _2892,
        _2939,
        _2977,
        _2983,
        _2986,
        _3004,
        _2935,
        _2974,
        _2874,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundSystemDeflection",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundSystemDeflection")


class AGMAGleasonConicalGearSetCompoundSystemDeflection(
    _2908.ConicalGearSetCompoundSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
            parent: "AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2908.ConicalGearSetCompoundSystemDeflection":
            return self._parent._cast(_2908.ConicalGearSetCompoundSystemDeflection)

        @property
        def gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2935.GearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2935,
            )

            return self._parent._cast(_2935.GearSetCompoundSystemDeflection)

        @property
        def specialised_assembly_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2974.SpecialisedAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.SpecialisedAssemblyCompoundSystemDeflection)

        @property
        def abstract_assembly_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2874.AbstractAssemblyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2874,
            )

            return self._parent._cast(_2874.AbstractAssemblyCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2887.BevelDifferentialGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2887,
            )

            return self._parent._cast(
                _2887.BevelDifferentialGearSetCompoundSystemDeflection
            )

        @property
        def bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2892.BevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.BevelGearSetCompoundSystemDeflection)

        @property
        def hypoid_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2939.HypoidGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.HypoidGearSetCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2977.SpiralBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.SpiralBevelGearSetCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2983.StraightBevelDiffGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2983,
            )

            return self._parent._cast(
                _2983.StraightBevelDiffGearSetCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_2986.StraightBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2986,
            )

            return self._parent._cast(
                _2986.StraightBevelGearSetCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "_3004.ZerolBevelGearSetCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3004,
            )

            return self._parent._cast(_3004.ZerolBevelGearSetCompoundSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_compound_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_2713.AGMAGleasonConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection]

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
    ) -> "List[_2713.AGMAGleasonConicalGearSetSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSetSystemDeflection]

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
    ) -> "AGMAGleasonConicalGearSetCompoundSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetCompoundSystemDeflection(self)
