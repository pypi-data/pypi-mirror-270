"""RollingRingCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "RollingRingCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2616
    from mastapy.system_model.analyses_and_results.system_deflections import _2822
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2952,
        _2899,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingCompoundSystemDeflection",)


Self = TypeVar("Self", bound="RollingRingCompoundSystemDeflection")


class RollingRingCompoundSystemDeflection(_2913.CouplingHalfCompoundSystemDeflection):
    """RollingRingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingCompoundSystemDeflection")

    class _Cast_RollingRingCompoundSystemDeflection:
        """Special nested class for casting RollingRingCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
            parent: "RollingRingCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_2913.CouplingHalfCompoundSystemDeflection":
            return self._parent._cast(_2913.CouplingHalfCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_2952.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2952,
            )

            return self._parent._cast(_2952.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_2899.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def rolling_ring_compound_system_deflection(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
        ) -> "RollingRingCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "RollingRingCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2616.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2822.RollingRingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[RollingRingCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.RollingRingCompoundSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2822.RollingRingSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

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
        "RollingRingCompoundSystemDeflection._Cast_RollingRingCompoundSystemDeflection"
    ):
        return self._Cast_RollingRingCompoundSystemDeflection(self)
