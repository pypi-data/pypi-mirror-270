"""CVTPulleyAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CVTPulleyAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7339,
        _7379,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CVTPulleyAdvancedSystemDeflection")


class CVTPulleyAdvancedSystemDeflection(_7390.PulleyAdvancedSystemDeflection):
    """CVTPulleyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyAdvancedSystemDeflection")

    class _Cast_CVTPulleyAdvancedSystemDeflection:
        """Special nested class for casting CVTPulleyAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
            parent: "CVTPulleyAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def pulley_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7390.PulleyAdvancedSystemDeflection":
            return self._parent._cast(_7390.PulleyAdvancedSystemDeflection)

        @property
        def coupling_half_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7339.CouplingHalfAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7339,
            )

            return self._parent._cast(_7339.CouplingHalfAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7379.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7379,
            )

            return self._parent._cast(_7379.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_pulley_advanced_system_deflection(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
        ) -> "CVTPulleyAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTPulleyAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTPulleyAdvancedSystemDeflection._Cast_CVTPulleyAdvancedSystemDeflection":
        return self._Cast_CVTPulleyAdvancedSystemDeflection(self)
