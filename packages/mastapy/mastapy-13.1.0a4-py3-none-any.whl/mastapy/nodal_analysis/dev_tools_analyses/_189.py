"""FEEntityGroup"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_ENTITY_GROUP = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses", "FEEntityGroup"
)

if TYPE_CHECKING:
    from mastapy.nodal_analysis.dev_tools_analyses import _187, _188, _190, _207
    from mastapy.nodal_analysis.component_mode_synthesis import _231, _232, _234


__docformat__ = "restructuredtext en"
__all__ = ("FEEntityGroup",)


Self = TypeVar("Self", bound="FEEntityGroup")
T = TypeVar("T")


class FEEntityGroup(_0.APIBase, Generic[T]):
    """FEEntityGroup

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _FE_ENTITY_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEEntityGroup")

    class _Cast_FEEntityGroup:
        """Special nested class for casting FEEntityGroup to subclasses."""

        def __init__(
            self: "FEEntityGroup._Cast_FEEntityGroup", parent: "FEEntityGroup"
        ):
            self._parent = parent

        @property
        def element_face_group(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_187.ElementFaceGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _187

            return self._parent._cast(_187.ElementFaceGroup)

        @property
        def element_group(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_188.ElementGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _188

            return self._parent._cast(_188.ElementGroup)

        @property
        def fe_entity_group_integer(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_190.FEEntityGroupInteger":
            from mastapy.nodal_analysis.dev_tools_analyses import _190

            return self._parent._cast(_190.FEEntityGroupInteger)

        @property
        def node_group(self: "FEEntityGroup._Cast_FEEntityGroup") -> "_207.NodeGroup":
            from mastapy.nodal_analysis.dev_tools_analyses import _207

            return self._parent._cast(_207.NodeGroup)

        @property
        def cms_element_face_group(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_231.CMSElementFaceGroup":
            from mastapy.nodal_analysis.component_mode_synthesis import _231

            return self._parent._cast(_231.CMSElementFaceGroup)

        @property
        def cms_element_face_group_of_all_free_faces(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_232.CMSElementFaceGroupOfAllFreeFaces":
            from mastapy.nodal_analysis.component_mode_synthesis import _232

            return self._parent._cast(_232.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def cms_node_group(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "_234.CMSNodeGroup":
            from mastapy.nodal_analysis.component_mode_synthesis import _234

            return self._parent._cast(_234.CMSNodeGroup)

        @property
        def fe_entity_group(
            self: "FEEntityGroup._Cast_FEEntityGroup",
        ) -> "FEEntityGroup":
            return self._parent

        def __getattr__(self: "FEEntityGroup._Cast_FEEntityGroup", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEEntityGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def number_of_items(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfItems

        if temp is None:
            return 0

        return temp

    @property
    def cast_to(self: Self) -> "FEEntityGroup._Cast_FEEntityGroup":
        return self._Cast_FEEntityGroup(self)
