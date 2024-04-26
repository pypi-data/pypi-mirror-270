"""ElmerResultsFromElectromagneticAnalysis"""

from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.elmer import _177
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELMER_RESULTS_FROM_ELECTROMAGNETIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.Elmer", "ElmerResultsFromElectromagneticAnalysis"
)


__docformat__ = "restructuredtext en"
__all__ = ("ElmerResultsFromElectromagneticAnalysis",)


Self = TypeVar("Self", bound="ElmerResultsFromElectromagneticAnalysis")


class ElmerResultsFromElectromagneticAnalysis(_177.ElmerResults):
    """ElmerResultsFromElectromagneticAnalysis

    This is a mastapy class.
    """

    TYPE = _ELMER_RESULTS_FROM_ELECTROMAGNETIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElmerResultsFromElectromagneticAnalysis"
    )

    class _Cast_ElmerResultsFromElectromagneticAnalysis:
        """Special nested class for casting ElmerResultsFromElectromagneticAnalysis to subclasses."""

        def __init__(
            self: "ElmerResultsFromElectromagneticAnalysis._Cast_ElmerResultsFromElectromagneticAnalysis",
            parent: "ElmerResultsFromElectromagneticAnalysis",
        ):
            self._parent = parent

        @property
        def elmer_results(
            self: "ElmerResultsFromElectromagneticAnalysis._Cast_ElmerResultsFromElectromagneticAnalysis",
        ) -> "_177.ElmerResults":
            return self._parent._cast(_177.ElmerResults)

        @property
        def elmer_results_from_electromagnetic_analysis(
            self: "ElmerResultsFromElectromagneticAnalysis._Cast_ElmerResultsFromElectromagneticAnalysis",
        ) -> "ElmerResultsFromElectromagneticAnalysis":
            return self._parent

        def __getattr__(
            self: "ElmerResultsFromElectromagneticAnalysis._Cast_ElmerResultsFromElectromagneticAnalysis",
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
        self: Self, instance_to_wrap: "ElmerResultsFromElectromagneticAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElmerResultsFromElectromagneticAnalysis._Cast_ElmerResultsFromElectromagneticAnalysis":
        return self._Cast_ElmerResultsFromElectromagneticAnalysis(self)
