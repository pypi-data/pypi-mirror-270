"""BarElasticMBD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.nodal_analysis.nodal_entities import _129
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BAR_ELASTIC_MBD = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.NodalEntities", "BarElasticMBD"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.nodal_entities import _134, _148, _149


__docformat__ = "restructuredtext en"
__all__ = ("BarElasticMBD",)


Self = TypeVar("Self", bound="BarElasticMBD")


class BarElasticMBD(_129.BarMBD):
    """BarElasticMBD

    This is a mastapy class.
    """

    TYPE = _BAR_ELASTIC_MBD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BarElasticMBD")

    class _Cast_BarElasticMBD:
        """Special nested class for casting BarElasticMBD to subclasses."""

        def __init__(
            self: "BarElasticMBD._Cast_BarElasticMBD", parent: "BarElasticMBD"
        ):
            self._parent = parent

        @property
        def bar_mbd(self: "BarElasticMBD._Cast_BarElasticMBD") -> "_129.BarMBD":
            return self._parent._cast(_129.BarMBD)

        @property
        def component_nodal_composite(
            self: "BarElasticMBD._Cast_BarElasticMBD",
        ) -> "_134.ComponentNodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _134

            return self._parent._cast(_134.ComponentNodalComposite)

        @property
        def nodal_composite(
            self: "BarElasticMBD._Cast_BarElasticMBD",
        ) -> "_148.NodalComposite":
            from mastapy.nodal_analysis.nodal_entities import _148

            return self._parent._cast(_148.NodalComposite)

        @property
        def nodal_entity(
            self: "BarElasticMBD._Cast_BarElasticMBD",
        ) -> "_149.NodalEntity":
            from mastapy.nodal_analysis.nodal_entities import _149

            return self._parent._cast(_149.NodalEntity)

        @property
        def bar_elastic_mbd(
            self: "BarElasticMBD._Cast_BarElasticMBD",
        ) -> "BarElasticMBD":
            return self._parent

        def __getattr__(self: "BarElasticMBD._Cast_BarElasticMBD", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BarElasticMBD.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "BarElasticMBD._Cast_BarElasticMBD":
        return self._Cast_BarElasticMBD(self)
