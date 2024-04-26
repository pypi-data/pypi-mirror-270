"""StepHalvingTransientSolver"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.system_solvers import _107
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STEP_HALVING_TRANSIENT_SOLVER = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.SystemSolvers", "StepHalvingTransientSolver"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.system_solvers import (
        _103,
        _108,
        _109,
        _112,
        _120,
        _119,
        _106,
        _118,
        _116,
    )


__docformat__ = "restructuredtext en"
__all__ = ("StepHalvingTransientSolver",)


Self = TypeVar("Self", bound="StepHalvingTransientSolver")


class StepHalvingTransientSolver(_107.InternalTransientSolver):
    """StepHalvingTransientSolver

    This is a mastapy class.
    """

    TYPE = _STEP_HALVING_TRANSIENT_SOLVER
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StepHalvingTransientSolver")

    class _Cast_StepHalvingTransientSolver:
        """Special nested class for casting StepHalvingTransientSolver to subclasses."""

        def __init__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            parent: "StepHalvingTransientSolver",
        ):
            self._parent = parent

        @property
        def internal_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_107.InternalTransientSolver":
            return self._parent._cast(_107.InternalTransientSolver)

        @property
        def transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_119.TransientSolver":
            from mastapy.nodal_analysis.system_solvers import _119

            return self._parent._cast(_119.TransientSolver)

        @property
        def dynamic_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_106.DynamicSolver":
            from mastapy.nodal_analysis.system_solvers import _106

            return self._parent._cast(_106.DynamicSolver)

        @property
        def stiffness_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_118.StiffnessSolver":
            from mastapy.nodal_analysis.system_solvers import _118

            return self._parent._cast(_118.StiffnessSolver)

        @property
        def solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_116.Solver":
            from mastapy.nodal_analysis.system_solvers import _116

            return self._parent._cast(_116.Solver)

        @property
        def backward_euler_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_103.BackwardEulerTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _103

            return self._parent._cast(_103.BackwardEulerTransientSolver)

        @property
        def lobatto_iiic_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_108.LobattoIIICTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _108

            return self._parent._cast(_108.LobattoIIICTransientSolver)

        @property
        def newmark_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_109.NewmarkTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _109

            return self._parent._cast(_109.NewmarkTransientSolver)

        @property
        def simple_velocity_based_step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_112.SimpleVelocityBasedStepHalvingTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _112

            return self._parent._cast(
                _112.SimpleVelocityBasedStepHalvingTransientSolver
            )

        @property
        def wilson_theta_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "_120.WilsonThetaTransientSolver":
            from mastapy.nodal_analysis.system_solvers import _120

            return self._parent._cast(_120.WilsonThetaTransientSolver)

        @property
        def step_halving_transient_solver(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
        ) -> "StepHalvingTransientSolver":
            return self._parent

        def __getattr__(
            self: "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StepHalvingTransientSolver.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "StepHalvingTransientSolver._Cast_StepHalvingTransientSolver":
        return self._Cast_StepHalvingTransientSolver(self)
