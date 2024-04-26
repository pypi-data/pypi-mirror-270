"""GearSetLoadDistributionAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1238
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.LTCA", "GearSetLoadDistributionAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.ltca.cylindrical import _867, _869
    from mastapy.gears.ltca.conical import _875
    from mastapy.gears.analysis import _1239, _1236, _1227


__docformat__ = "restructuredtext en"
__all__ = ("GearSetLoadDistributionAnalysis",)


Self = TypeVar("Self", bound="GearSetLoadDistributionAnalysis")


class GearSetLoadDistributionAnalysis(_1238.GearSetImplementationAnalysis):
    """GearSetLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_LOAD_DISTRIBUTION_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearSetLoadDistributionAnalysis")

    class _Cast_GearSetLoadDistributionAnalysis:
        """Special nested class for casting GearSetLoadDistributionAnalysis to subclasses."""

        def __init__(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
            parent: "GearSetLoadDistributionAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_1238.GearSetImplementationAnalysis":
            return self._parent._cast(_1238.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_1239.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1239

            return self._parent._cast(_1239.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def cylindrical_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_867.CylindricalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _867

            return self._parent._cast(_867.CylindricalGearSetLoadDistributionAnalysis)

        @property
        def face_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_869.FaceGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.cylindrical import _869

            return self._parent._cast(_869.FaceGearSetLoadDistributionAnalysis)

        @property
        def conical_gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "_875.ConicalGearSetLoadDistributionAnalysis":
            from mastapy.gears.ltca.conical import _875

            return self._parent._cast(_875.ConicalGearSetLoadDistributionAnalysis)

        @property
        def gear_set_load_distribution_analysis(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
        ) -> "GearSetLoadDistributionAnalysis":
            return self._parent

        def __getattr__(
            self: "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearSetLoadDistributionAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_a_system_deflection_analysis(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsASystemDeflectionAnalysis

        if temp is None:
            return False

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "GearSetLoadDistributionAnalysis._Cast_GearSetLoadDistributionAnalysis":
        return self._Cast_GearSetLoadDistributionAnalysis(self)
