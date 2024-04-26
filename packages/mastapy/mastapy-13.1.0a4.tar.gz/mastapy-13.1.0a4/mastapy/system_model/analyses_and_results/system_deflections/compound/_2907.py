"""ConicalGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2934
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ConicalGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2747
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2879,
        _2886,
        _2891,
        _2938,
        _2942,
        _2945,
        _2948,
        _2976,
        _2982,
        _2985,
        _3003,
        _2940,
        _2909,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ConicalGearMeshCompoundSystemDeflection")


class ConicalGearMeshCompoundSystemDeflection(_2934.GearMeshCompoundSystemDeflection):
    """ConicalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConicalGearMeshCompoundSystemDeflection"
    )

    class _Cast_ConicalGearMeshCompoundSystemDeflection:
        """Special nested class for casting ConicalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
            parent: "ConicalGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2934.GearMeshCompoundSystemDeflection":
            return self._parent._cast(_2934.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2940.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(
                _2940.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2909.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2909,
            )

            return self._parent._cast(_2909.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2879.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2879,
            )

            return self._parent._cast(
                _2879.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2886.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(
                _2886.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2891.BevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2891,
            )

            return self._parent._cast(_2891.BevelGearMeshCompoundSystemDeflection)

        @property
        def hypoid_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2938.HypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2938,
            )

            return self._parent._cast(_2938.HypoidGearMeshCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2942.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(
                _2942.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2945.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2945,
            )

            return self._parent._cast(
                _2945.KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> (
            "_2948.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2948,
            )

            return self._parent._cast(
                _2948.KlingelnbergCycloPalloidSpiralBevelGearMeshCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2976.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2982.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(
                _2982.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_2985.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2985,
            )

            return self._parent._cast(
                _2985.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "_3003.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _3003,
            )

            return self._parent._cast(_3003.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
        ) -> "ConicalGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ConicalGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.ConicalGearMeshCompoundSystemDeflection]

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
    ) -> "List[_2747.ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

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
    ) -> "List[_2747.ConicalGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ConicalGearMeshSystemDeflection]

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
    ) -> "ConicalGearMeshCompoundSystemDeflection._Cast_ConicalGearMeshCompoundSystemDeflection":
        return self._Cast_ConicalGearMeshCompoundSystemDeflection(self)
