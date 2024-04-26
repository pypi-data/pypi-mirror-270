"""HypoidGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7437,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "HypoidGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7364,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7465,
        _7491,
        _7497,
        _7467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="HypoidGearMeshCompoundAdvancedSystemDeflection")


class HypoidGearMeshCompoundAdvancedSystemDeflection(
    _7437.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
):
    """HypoidGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_HypoidGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting HypoidGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
            parent: "HypoidGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7437.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7437.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7465.ConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.ConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7491.GearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7491,
            )

            return self._parent._cast(_7491.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(
                _7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7467.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
        ) -> "HypoidGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "HypoidGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2333.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

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
    ) -> "List[_7364.HypoidGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearMeshAdvancedSystemDeflection]

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
    ) -> "List[_7364.HypoidGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.HypoidGearMeshAdvancedSystemDeflection]

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
    ) -> "HypoidGearMeshCompoundAdvancedSystemDeflection._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_HypoidGearMeshCompoundAdvancedSystemDeflection(self)
