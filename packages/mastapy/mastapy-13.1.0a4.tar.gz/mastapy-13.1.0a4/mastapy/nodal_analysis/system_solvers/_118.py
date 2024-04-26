"""StiffnessSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _116
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STIFFNESS_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "StiffnessSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _105,
        _106,
        _107,
        _108,
        _109,
        _112,
        _117,
        _119,
        _120,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StiffnessSolver",)


Self = TypeVar("Self", bound="StiffnessSolver")


class StiffnessSolver(_116.Solver):
    """StiffnessSolver

    This is a mastapy class.
    """

    TYPE = _STIFFNESS_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StiffnessSolver")

    class _Cast_StiffnessSolver:
        """Special nested class for casting StiffnessSolver to subclasses."""

        def __init__(
            self: "StiffnessSolver._Cast_StiffnessSolver", parent: "StiffnessSolver"
        ):
            self._parent = parent

        @property
        def solver(self: "StiffnessSolver._Cast_StiffnessSolver") -> "_116.Solver":
            return self._parent._cast(_116.Solver)

        @property
        def backward_euler_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_103.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.BackwardEulerTransientSolver)

        @property
        def dirk_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_105.DirkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _105

            return self._parent._cast(_105.DirkTransientSolver)

        @property
        def dynamic_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def internal_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_107.InternalTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _107

            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_108.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIICTransientSolver)

        @property
        def newmark_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_109.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_112.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(
                _112.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def step_halving_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_117.StepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _117

            return self._parent._cast(_117.StepHalvingTransientSolver)

        @property
        def transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_119.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.TransientSolver)

        @property
        def wilson_theta_transient_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "_120.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.WilsonThetaTransientSolver)

        @property
        def stiffness_solver(
            self: "StiffnessSolver._Cast_StiffnessSolver",
        ) -> "StiffnessSolver":
            return self._parent

        def __getattr__(self: "StiffnessSolver._Cast_StiffnessSolver", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StiffnessSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "StiffnessSolver._Cast_StiffnessSolver":
        return self._Cast_StiffnessSolver(self)
