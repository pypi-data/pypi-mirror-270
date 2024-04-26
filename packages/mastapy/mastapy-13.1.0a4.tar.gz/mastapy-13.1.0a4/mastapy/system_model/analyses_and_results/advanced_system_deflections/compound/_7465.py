"""ConicalGearMeshCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7491,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "ConicalGearMeshCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7332,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7437,
        _7444,
        _7449,
        _7495,
        _7499,
        _7502,
        _7505,
        _7532,
        _7538,
        _7541,
        _7559,
        _7497,
        _7467,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundAdvancedSystemDeflection")


class ConicalGearMeshCompoundAdvancedSystemDeflection(
    _7491.GearMeshCompoundAdvancedSystemDeflection
):
    """ConicalGearMeshCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundAdvancedSystemDeflection"
    )

    class _Cast_ConicalGearMeshCompoundAdvancedSystemDeflection:
        """Special nested class for casting ConicalGearMeshCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
            parent: "ConicalGearMeshCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7491.GearMeshCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7491.GearMeshCompoundAdvancedSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(
                _7497.InterMountableComponentConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def connection_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7467.ConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7467,
            )

            return self._parent._cast(_7467.ConnectionCompoundAdvancedSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7437.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(
                _7437.AGMAGleasonConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7444.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(
                _7444.BevelDifferentialGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7449.BevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(
                _7449.BevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7495.HypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(
                _7495.HypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7499.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.KlingelnbergCycloPalloidConicalGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7502.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.KlingelnbergCycloPalloidHypoidGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7505.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7505,
            )

            return self._parent._cast(
                _7505.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7532.SpiralBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7532,
            )

            return self._parent._cast(
                _7532.SpiralBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7538.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7538,
            )

            return self._parent._cast(
                _7538.StraightBevelDiffGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7541.StraightBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7541,
            )

            return self._parent._cast(
                _7541.StraightBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "_7559.ZerolBevelGearMeshCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7559,
            )

            return self._parent._cast(
                _7559.ZerolBevelGearMeshCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_advanced_system_deflection(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
        ) -> "ConicalGearMeshCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "ConicalGearMeshCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(
        self: Self,
    ) -> "List[ConicalGearMeshCompoundAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.compound.ConicalGearMeshCompoundAdvancedSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7332.ConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearMeshAdvancedSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7332.ConicalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.ConicalGearMeshAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "ConicalGearMeshCompoundAdvancedSystemDeflection._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection":
        return self._Cast_ConicalGearMeshCompoundAdvancedSystemDeflection(self)
