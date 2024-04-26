"""ConicalSetManufacturingAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1238
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MANUFACTURING_ANALYSIS = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalSetManufacturingAnalysis"
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1239, _1236, _1227


__docformat__ = "restructuredtext en"
__all__ = ("ConicalSetManufacturingAnalysis",)


Self = TypeVar("Self", bound="ConicalSetManufacturingAnalysis")


class ConicalSetManufacturingAnalysis(_1238.GearSetImplementationAnalysis):
    """ConicalSetManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MANUFACTURING_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalSetManufacturingAnalysis")

    class _Cast_ConicalSetManufacturingAnalysis:
        """Special nested class for casting ConicalSetManufacturingAnalysis to subclasses."""

        def __init__(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
            parent: "ConicalSetManufacturingAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_implementation_analysis(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
        ) -> "_1238.GearSetImplementationAnalysis":
            return self._parent._cast(_1238.GearSetImplementationAnalysis)

        @property
        def gear_set_implementation_analysis_abstract(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
        ) -> "_1239.GearSetImplementationAnalysisAbstract":
            from mastapy.gears.analysis import _1239

            return self._parent._cast(_1239.GearSetImplementationAnalysisAbstract)

        @property
        def gear_set_design_analysis(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
        ) -> "_1236.GearSetDesignAnalysis":
            from mastapy.gears.analysis import _1236

            return self._parent._cast(_1236.GearSetDesignAnalysis)

        @property
        def abstract_gear_set_analysis(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
        ) -> "_1227.AbstractGearSetAnalysis":
            from mastapy.gears.analysis import _1227

            return self._parent._cast(_1227.AbstractGearSetAnalysis)

        @property
        def conical_set_manufacturing_analysis(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
        ) -> "ConicalSetManufacturingAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalSetManufacturingAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalSetManufacturingAnalysis._Cast_ConicalSetManufacturingAnalysis":
        return self._Cast_ConicalSetManufacturingAnalysis(self)
