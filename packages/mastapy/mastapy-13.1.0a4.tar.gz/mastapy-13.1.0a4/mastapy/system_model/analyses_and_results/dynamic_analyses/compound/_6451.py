"""BevelGearMeshCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6439
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "BevelGearMeshCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6446,
        _6534,
        _6540,
        _6543,
        _6561,
        _6467,
        _6493,
        _6499,
        _6469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundDynamicAnalysis")


class BevelGearMeshCompoundDynamicAnalysis(
    _6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
):
    """BevelGearMeshCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCompoundDynamicAnalysis")

    class _Cast_BevelGearMeshCompoundDynamicAnalysis:
        """Special nested class for casting BevelGearMeshCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
            parent: "BevelGearMeshCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis":
            return self._parent._cast(
                _6439.AGMAGleasonConicalGearMeshCompoundDynamicAnalysis
            )

        @property
        def conical_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6467.ConicalGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6467,
            )

            return self._parent._cast(_6467.ConicalGearMeshCompoundDynamicAnalysis)

        @property
        def gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6493.GearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6493,
            )

            return self._parent._cast(_6493.GearMeshCompoundDynamicAnalysis)

        @property
        def inter_mountable_component_connection_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6499.InterMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6499,
            )

            return self._parent._cast(
                _6499.InterMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6469.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6469,
            )

            return self._parent._cast(_6469.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6446.BevelDifferentialGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6446,
            )

            return self._parent._cast(
                _6446.BevelDifferentialGearMeshCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6534.SpiralBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6534,
            )

            return self._parent._cast(_6534.SpiralBevelGearMeshCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6540,
            )

            return self._parent._cast(
                _6540.StraightBevelDiffGearMeshCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6543.StraightBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6543,
            )

            return self._parent._cast(
                _6543.StraightBevelGearMeshCompoundDynamicAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "_6561.ZerolBevelGearMeshCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6561,
            )

            return self._parent._cast(_6561.ZerolBevelGearMeshCompoundDynamicAnalysis)

        @property
        def bevel_gear_mesh_compound_dynamic_analysis(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
        ) -> "BevelGearMeshCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6320.BevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis]

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
    ) -> "List[_6320.BevelGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.BevelGearMeshDynamicAnalysis]

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
    ) -> "BevelGearMeshCompoundDynamicAnalysis._Cast_BevelGearMeshCompoundDynamicAnalysis":
        return self._Cast_BevelGearMeshCompoundDynamicAnalysis(self)
