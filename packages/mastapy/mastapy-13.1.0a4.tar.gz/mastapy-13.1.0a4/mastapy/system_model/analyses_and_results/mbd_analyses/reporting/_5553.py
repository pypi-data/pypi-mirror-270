"""NodeInformation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NODE_INFORMATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting",
    "NodeInformation",
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _75


__docformat__ = "restructuredtext en"
__all__ = ("NodeInformation",)


Self = TypeVar("Self", bound="NodeInformation")


class NodeInformation(_0.APIBase):
    """NodeInformation

    This is a mastapy class.
    """

    TYPE = _NODE_INFORMATION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NodeInformation")

    class _Cast_NodeInformation:
        """Special nested class for casting NodeInformation to subclasses."""

        def __init__(
            self: "NodeInformation._Cast_NodeInformation", parent: "NodeInformation"
        ):
            self._parent = parent

        @property
        def node_information(
            self: "NodeInformation._Cast_NodeInformation",
        ) -> "NodeInformation":
            return self._parent

        def __getattr__(self: "NodeInformation._Cast_NodeInformation", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NodeInformation.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def node_id(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeID

        if temp is None:
            return 0

        return temp

    @property
    def parts_using_node(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PartsUsingNode

        if temp is None:
            return ""

        return temp

    @property
    def node_info(self: Self) -> "_75.LocalNodeInfo":
        """mastapy.nodal_analysis.LocalNodeInfo

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeInfo

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "NodeInformation._Cast_NodeInformation":
        return self._Cast_NodeInformation(self)
