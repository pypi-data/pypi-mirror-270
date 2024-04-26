"""TorqueConverterConnectionAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7338
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "TorqueConverterConnectionAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2370
    from mastapy.system_model.analyses_and_results.static_loads import _6999
    from mastapy.system_model.analyses_and_results.system_deflections import _2851
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7366,
        _7334,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7567, _7564
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterConnectionAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="TorqueConverterConnectionAdvancedSystemDeflection")


class TorqueConverterConnectionAdvancedSystemDeflection(
    _7338.CouplingConnectionAdvancedSystemDeflection
):
    """TorqueConverterConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_CONNECTION_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterConnectionAdvancedSystemDeflection"
    )

    class _Cast_TorqueConverterConnectionAdvancedSystemDeflection:
        """Special nested class for casting TorqueConverterConnectionAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
            parent: "TorqueConverterConnectionAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def coupling_connection_advanced_system_deflection(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_7338.CouplingConnectionAdvancedSystemDeflection":
            return self._parent._cast(_7338.CouplingConnectionAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_advanced_system_deflection(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_7366.InterMountableComponentConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7366,
            )

            return self._parent._cast(
                _7366.InterMountableComponentConnectionAdvancedSystemDeflection
            )

        @property
        def connection_advanced_system_deflection(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_7334.ConnectionAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7334,
            )

            return self._parent._cast(_7334.ConnectionAdvancedSystemDeflection)

        @property
        def connection_static_load_analysis_case(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def torque_converter_connection_advanced_system_deflection(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
        ) -> "TorqueConverterConnectionAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection",
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
        instance_to_wrap: "TorqueConverterConnectionAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2370.TorqueConverterConnection":
        """mastapy.system_model.connections_and_sockets.couplings.TorqueConverterConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6999.TorqueConverterConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.TorqueConverterConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_system_deflection_results(
        self: Self,
    ) -> "List[_2851.TorqueConverterConnectionSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.TorqueConverterConnectionSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionSystemDeflectionResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterConnectionAdvancedSystemDeflection._Cast_TorqueConverterConnectionAdvancedSystemDeflection":
        return self._Cast_TorqueConverterConnectionAdvancedSystemDeflection(self)
