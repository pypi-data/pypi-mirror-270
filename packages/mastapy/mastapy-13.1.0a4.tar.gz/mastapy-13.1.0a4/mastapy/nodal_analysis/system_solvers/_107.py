"""InternalTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _119
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTERNAL_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "InternalTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _105,
        _108,
        _109,
        _112,
        _117,
        _120,
        _106,
        _118,
        _116,
    )


__docformat__ = "restructuredtext en"
__all__ = ("InternalTransientSolver",)


Self = TypeVar("Self", bound="InternalTransientSolver")


class InternalTransientSolver(_119.TransientSolver):
    """InternalTransientSolver

    This is a mastapy class.
    """

    TYPE = _INTERNAL_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_InternalTransientSolver")

    class _Cast_InternalTransientSolver:
        """Special nested class for casting InternalTransientSolver to subclasses."""

        def __init__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
            parent: "InternalTransientSolver",
        ):
            self._parent = parent

        @property
        def transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_119.TransientSolver":
            return self._parent._cast(_119.TransientSolver)

        @property
        def dynamic_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_118.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.StiffnessSolver)

        @property
        def solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_116.Solver":
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.Solver)

        @property
        def backward_euler_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_103.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.BackwardEulerTransientSolver)

        @property
        def dirk_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_105.DirkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.DirkTransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_108.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIICTransientSolver)

        @property
        def newmark_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_109.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_112.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(
                _112.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_117.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StepHalvingTransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "_120.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.WilsonThetaTransientSolver)

        @property
        def internal_transient_solver(
            self: "InternalTransientSolver._Cast_InternalTransientSolver",
        ) -> "InternalTransientSolver":
            return self._parent

        def __getattr__(
            self: "InternalTransientSolver._Cast_InternalTransientSolver", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "InternalTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "InternalTransientSolver._Cast_InternalTransientSolver":
        return self._Cast_InternalTransientSolver(self)
