"""CVTBeltConnectionSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2722
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CVTBeltConnectionSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2291
    from mastapy.system_model.analyses_and_results.power_flows import _4095
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2790,
        _2750,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7566,
        _7567,
        _7564,
    )
    from mastapy.system_model.analyses_and_results import _2672, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CVTBeltConnectionSystemDeflection",)


Self = TypeVar("Self", bound="CVTBeltConnectionSystemDeflection")


class CVTBeltConnectionSystemDeflection(_2722.BeltConnectionSystemDeflection):
    """CVTBeltConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTBeltConnectionSystemDeflection")

    class _Cast_CVTBeltConnectionSystemDeflection:
        """Special nested class for casting CVTBeltConnectionSystemDeflection to subclasses."""

        def __init__(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
            parent: "CVTBeltConnectionSystemDeflection",
        ):
            self._parent = parent

        @property
        def belt_connection_system_deflection(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2722.BeltConnectionSystemDeflection":
            return self._parent._cast(_2722.BeltConnectionSystemDeflection)

        @property
        def inter_mountable_component_connection_system_deflection(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2790.InterMountableComponentConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(
                _2790.InterMountableComponentConnectionSystemDeflection
            )

        @property
        def connection_system_deflection(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2750.ConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2750,
            )

            return self._parent._cast(_2750.ConnectionSystemDeflection)

        @property
        def connection_fe_analysis(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_7566.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7566

            return self._parent._cast(_7566.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_7567.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7567

            return self._parent._cast(_7567.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_7564.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7564

            return self._parent._cast(_7564.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2672.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2672

            return self._parent._cast(_2672.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_system_deflection(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
        ) -> "CVTBeltConnectionSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection",
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
        self: Self, instance_to_wrap: "CVTBeltConnectionSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_clamping_force_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeltClampingForceSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_required_clamping_force(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRequiredClampingForce

        if temp is None:
            return 0.0

        return temp

    @property
    def pump_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PumpEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def total_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TotalEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def variator_efficiency(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.VariatorEfficiency

        if temp is None:
            return 0.0

        return temp

    @property
    def connection_design(self: Self) -> "_2291.CVTBeltConnection":
        """mastapy.system_model.connections_and_sockets.CVTBeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4095.CVTBeltConnectionPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.CVTBeltConnectionPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTBeltConnectionSystemDeflection._Cast_CVTBeltConnectionSystemDeflection":
        return self._Cast_CVTBeltConnectionSystemDeflection(self)
