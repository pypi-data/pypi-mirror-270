"""ElectricMachineFEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines.load_cases_and_analyses import _1382
from mastapy.electric_machines.results import _1351
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses", "ElectricMachineFEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.electric_machines.results import _1333
    from mastapy.nodal_analysis.elmer import _179
    from mastapy.electric_machines.load_cases_and_analyses import _1364


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineFEAnalysis",)


Self = TypeVar("Self", bound="ElectricMachineFEAnalysis")


class ElectricMachineFEAnalysis(
    _1382.SingleOperatingPointAnalysis, _1351.IHaveDynamicForceResults
):
    """ElectricMachineFEAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ElectricMachineFEAnalysis")

    class _Cast_ElectricMachineFEAnalysis:
        """Special nested class for casting ElectricMachineFEAnalysis to subclasses."""

        def __init__(
            self: "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis",
            parent: "ElectricMachineFEAnalysis",
        ):
            self._parent = parent

        @property
        def single_operating_point_analysis(
            self: "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis",
        ) -> "_1382.SingleOperatingPointAnalysis":
            return self._parent._cast(_1382.SingleOperatingPointAnalysis)

        @property
        def electric_machine_analysis(
            self: "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis",
        ) -> "_1364.ElectricMachineAnalysis":
            from mastapy.electric_machines.load_cases_and_analyses import _1364

            return self._parent._cast(_1364.ElectricMachineAnalysis)

        @property
        def electric_machine_fe_analysis(
            self: "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis",
        ) -> "ElectricMachineFEAnalysis":
            return self._parent

        def __getattr__(
            self: "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ElectricMachineFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electromagnetic_solver_analysis_time(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ElectromagneticSolverAnalysisTime

        if temp is None:
            return 0.0

        return temp

    @property
    def dynamic_force_results(self: Self) -> "_1333.DynamicForceResults":
        """mastapy.electric_machines.results.DynamicForceResults

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DynamicForceResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def viewable(self: Self) -> "_179.ElmerResultsViewable":
        """mastapy.nodal_analysis.elmer.ElmerResultsViewable

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Viewable

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineFEAnalysis._Cast_ElectricMachineFEAnalysis":
        return self._Cast_ElectricMachineFEAnalysis(self)
