"""ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5558
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5511
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5579,
        _5599,
        _5638,
        _5590,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
)


class ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5558.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
):
    """ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5558.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5558.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5590,
            )

            return self._parent._cast(_5590.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5579.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(
                _5579.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5511.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5511.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
