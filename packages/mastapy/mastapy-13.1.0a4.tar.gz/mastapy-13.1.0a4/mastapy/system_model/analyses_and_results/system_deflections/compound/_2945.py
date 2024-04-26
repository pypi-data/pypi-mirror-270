"""KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2942
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2337
    from mastapy.system_model.analyses_and_results.system_deflections import _2794
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2907,
        _2934,
        _2940,
        _2909,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection(
    _2942.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2942.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            return self._parent._cast(
                _2942.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2907.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2934.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2934,
            )

            return self._parent._cast(_2934.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2940.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2909.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2337.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2794.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection(
                self
            )
        )
