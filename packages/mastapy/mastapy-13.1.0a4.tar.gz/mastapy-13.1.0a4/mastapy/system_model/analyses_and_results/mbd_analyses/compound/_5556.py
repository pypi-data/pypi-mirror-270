"""AbstractShaftCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5557
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "AbstractShaftCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5400
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5600,
        _5650,
        _5580,
        _5634,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7572, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundMultibodyDynamicsAnalysis")


class AbstractShaftCompoundMultibodyDynamicsAnalysis(
    _5557.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
):
    """AbstractShaftCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting AbstractShaftCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
            parent: "AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_5557.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5557.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_5580.ComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5580,
            )

            return self._parent._cast(_5580.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_5634.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5634,
            )

            return self._parent._cast(_5634.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_7572.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7572

            return self._parent._cast(_7572.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_5600.CycloidalDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.CycloidalDiscCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.ShaftCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(_5650.ShaftCompoundMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_compound_multibody_dynamics_analysis(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
        ) -> "AbstractShaftCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "AbstractShaftCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5400.AbstractShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5400.AbstractShaftMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.AbstractShaftMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftCompoundMultibodyDynamicsAnalysis._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis":
        return self._Cast_AbstractShaftCompoundMultibodyDynamicsAnalysis(self)
