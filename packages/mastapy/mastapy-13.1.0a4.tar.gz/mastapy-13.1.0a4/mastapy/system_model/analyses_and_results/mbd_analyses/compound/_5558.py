"""AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5402
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5579,
        _5599,
        _5601,
        _5638,
        _5652,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
)


class AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
    _5590.ConnectionCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.ConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5590.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5579.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5579,
            )

            return self._parent._cast(
                _5579.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5599.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5599,
            )

            return self._parent._cast(
                _5599.CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5601.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5601,
            )

            return self._parent._cast(
                _5601.CycloidalDiscPlanetaryBearingConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5638.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5638,
            )

            return self._parent._cast(
                _5638.PlanetaryConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5652.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5402.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5402.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis]

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
    ) -> "AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
