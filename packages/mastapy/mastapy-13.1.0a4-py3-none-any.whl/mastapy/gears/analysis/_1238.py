"""GearSetImplementationAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.analysis import _1239
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_IMPLEMENTATION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearSetImplementationAnalysis"
)

if TYPE_CHECKING:
    from mastapy import _7585
    from mastapy.gears.manufacturing.cylindrical import _628
    from mastapy.gears.manufacturing.bevel import _797
    from mastapy.gears.ltca import _853
    from mastapy.gears.ltca.cylindrical import _867, _869
    from mastapy.gears.ltca.conical import _875
    from mastapy.gears.analysis import _1236, _1227


__docformat__ = "restructuredtext en"
__all__ = ("GearSetImplementationAnalysis",)


Self = TypeVar("Self", bound="GearSetImplementationAnalysis")


class GearSetImplementationAnalysis(_1239.GearSetImplementationAnalysisAbstract):
    """GearSetImplementationAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_IMPLEMENTATION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetImplementationAnalysis")

    class _Cast_GearSetImplementationAnalysis:
        """Special nested class for casting GearSetImplementationAnalysis to subclasses."""

        def __init__(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
            parent: "GearSetImplementationAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1239.GearSetImplementationAnalysisAbstract":
            return self._parent._cast(_1239.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def cylindrical_manufactured_gear_set_load_case(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_628.CylindricalManufacturedGearSetLoadCase":
            from mastapy.gears.manufacturing.cylindrical import _628

            return self._parent._cast(_628.CylindricalManufacturedGearSetLoadCase)

        @property
        def conical_set_manufacturing_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_797.ConicalSetManufacturingAnalysis":
            from mastapy.gears.manufacturing.bevel import _797

            return self._parent._cast(_797.ConicalSetManufacturingAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_853.GearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca import _853

            return self._parent._cast(_853.GearSetLoadDistributionAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_867.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _867

            return self._parent._cast(_867.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_869.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _869

            return self._parent._cast(_869.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "_875.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_implementation_analysis(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
        ) -> "GearSetImplementationAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetImplementationAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def valid_results_ready(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ValidResultsReady

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def perform_analysis(self: Self, run_all_planetary_meshes: "bool" = True):
        """Method does not return.

        Args:
            run_all_planetary_meshes (bool, optional)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysis(
            run_all_planetary_meshes if run_all_planetary_meshes else False
        )

    @enforce_parameter_types
    def perform_analysis_with_progress(
        self: Self, run_all_planetary_meshes: "bool", progress: "_7585.TaskProgress"
    ):
        """Method does not return.

        Args:
            run_all_planetary_meshes (bool)
            progress (mastapy.TaskProgress)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        self.wrapped.PerformAnalysisWithProgress(
            run_all_planetary_meshes if run_all_planetary_meshes else False,
            progress.wrapped if progress else None,
        )

    @enforce_parameter_types
    def results_ready_for(
        self: Self, run_all_planetary_meshes: "bool" = True
    ) -> "bool":
        """bool

        Args:
            run_all_planetary_meshes (bool, optional)
        """
        run_all_planetary_meshes = bool(run_all_planetary_meshes)
        method_result = self.wrapped.ResultsReadyFor(
            run_all_planetary_meshes if run_all_planetary_meshes else False
        )
        return method_result

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetImplementationAnalysis._Cast_GearSetImplementationAnalysis":
        return self._Cast_GearSetImplementationAnalysis(self)
