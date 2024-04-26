"""VirtualComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2952
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "VirtualComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2858
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2950,
        _2951,
        _2961,
        _2962,
        _2997,
        _2899,
        _2954,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundSystemDeflection")


class VirtualComponentCompoundSystemDeflection(
    _2952.MountableComponentCompoundSystemDeflection
):
    """VirtualComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
            parent: "VirtualComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2952.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2952.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2899.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2899,
            )

            return self._parent._cast(_2899.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2954.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def mass_disc_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2950.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2950,
            )

            return self._parent._cast(_2950.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2951.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(
                _2951.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def point_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2961.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(_2961.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2962.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2962,
            )

            return self._parent._cast(_2962.PowerLoadCompoundSystemDeflection)

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2997.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2997,
            )

            return self._parent._cast(_2997.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "VirtualComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2858.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2858.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection":
        return self._Cast_VirtualComponentCompoundSystemDeflection(self)
