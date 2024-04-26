"""DirkTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _107
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DIRK_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "DirkTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import _119, _106, _118, _116


__docformat__ = "restructuredtext en"
__all__ = ("DirkTransientSolver",)


Self = TypeVar("Self", bound="DirkTransientSolver")


class DirkTransientSolver(_107.InternalTransientSolver):
    """DirkTransientSolver

    This is a mastapy class.
    """

    TYPE = _DIRK_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DirkTransientSolver")

    class _Cast_DirkTransientSolver:
        """Special nested class for casting DirkTransientSolver to subclasses."""

        def __init__(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
            parent: "DirkTransientSolver",
        ):
            self._parent = parent

        @property
        def internal_transient_solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "_107.InternalTransientSolver":
            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "_119.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.TransientSolver)

        @property
        def dynamic_solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "_118.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.StiffnessSolver)

        @property
        def solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "_116.Solver":
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.Solver)

        @property
        def dirk_transient_solver(
            self: "DirkTransientSolver._Cast_DirkTransientSolver",
        ) -> "DirkTransientSolver":
            return self._parent

        def __getattr__(
            self: "DirkTransientSolver._Cast_DirkTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DirkTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DirkTransientSolver._Cast_DirkTransientSolver":
        return self._Cast_DirkTransientSolver(self)
