"""AbstractShaftAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7298
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AbstractShaftAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2453
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7344,
        _7397,
        _7324,
        _7381,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7574, _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftAdvancedSystemDeflection")


class AbstractShaftAdvancedSystemDeflection(
    _7298.AbstractShaftOrHousingAdvancedSystemDeflection
):
    """AbstractShaftAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftAdvancedSystemDeflection"
    )

    class _Cast_AbstractShaftAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
            parent: "AbstractShaftAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7298.AbstractShaftOrHousingAdvancedSystemDeflection":
            return self._parent._cast(
                _7298.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def component_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7324.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7324,
            )

            return self._parent._cast(_7324.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7381.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7381,
            )

            return self._parent._cast(_7381.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7574.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7574

            return self._parent._cast(_7574.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7344.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7344,
            )

            return self._parent._cast(_7344.CycloidalDiscAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7397.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7397,
            )

            return self._parent._cast(_7397.ShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "AbstractShaftAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractShaftAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2453.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

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
    ) -> "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection":
        return self._Cast_AbstractShaftAdvancedSystemDeflection(self)
