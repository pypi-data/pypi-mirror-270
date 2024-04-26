"""DynamicSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _118
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DYNAMIC_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "DynamicSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _105,
        _107,
        _108,
        _109,
        _112,
        _117,
        _119,
        _120,
        _116,
    )


__docformat__ = "restructuredtext en"
__all__ = ("DynamicSolver",)


Self = TypeVar("Self", bound="DynamicSolver")


class DynamicSolver(_118.StiffnessSolver):
    """DynamicSolver

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DynamicSolver")

    class _Cast_DynamicSolver:
        """Special nested class for casting DynamicSolver to subclasses."""

        def __init__(
            self: "DynamicSolver._Cast_DynamicSolver", parent: "DynamicSolver"
        ):
            self._parent = parent

        @property
        def stiffness_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_118.StiffnessSolver":
            return self._parent._cast(_118.StiffnessSolver)

        @property
        def solver(self: "DynamicSolver._Cast_DynamicSolver") -> "_116.Solver":
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.Solver)

        @property
        def backward_euler_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_103.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.BackwardEulerTransientSolver)

        @property
        def dirk_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_105.DirkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.DirkTransientSolver)

        @property
        def internal_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_108.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIICTransientSolver)

        @property
        def newmark_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_109.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_112.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(
                _112.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_117.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StepHalvingTransientSolver)

        @property
        def transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_119.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.TransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "_120.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.WilsonThetaTransientSolver)

        @property
        def dynamic_solver(
            self: "DynamicSolver._Cast_DynamicSolver",
        ) -> "DynamicSolver":
            return self._parent

        def __getattr__(self: "DynamicSolver._Cast_DynamicSolver", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DynamicSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "DynamicSolver._Cast_DynamicSolver":
        return self._Cast_DynamicSolver(self)
