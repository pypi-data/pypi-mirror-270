"""ConceptGearMeshCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4525,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "ConceptGearMeshCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2323
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4348
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4531,
        _4501,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7565, _7569
    from mastapy.system_model.analyses_and_results import _2674


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="ConceptGearMeshCompoundParametricStudyTool")


class ConceptGearMeshCompoundParametricStudyTool(
    _4525.GearMeshCompoundParametricStudyTool
):
    """ConceptGearMeshCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshCompoundParametricStudyTool"
    )

    class _Cast_ConceptGearMeshCompoundParametricStudyTool:
        """Special nested class for casting ConceptGearMeshCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
            parent: "ConceptGearMeshCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_parametric_study_tool(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_4525.GearMeshCompoundParametricStudyTool":
            return self._parent._cast(_4525.GearMeshCompoundParametricStudyTool)

        @property
        def inter_mountable_component_connection_compound_parametric_study_tool(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_4531.InterMountableComponentConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4531,
            )

            return self._parent._cast(
                _4531.InterMountableComponentConnectionCompoundParametricStudyTool
            )

        @property
        def connection_compound_parametric_study_tool(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_4501.ConnectionCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4501,
            )

            return self._parent._cast(_4501.ConnectionCompoundParametricStudyTool)

        @property
        def connection_compound_analysis(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_7565.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7565

            return self._parent._cast(_7565.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_7569.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7569

            return self._parent._cast(_7569.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_compound_parametric_study_tool(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
        ) -> "ConceptGearMeshCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "ConceptGearMeshCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2323.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2323.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_4348.ConceptGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_4348.ConceptGearMeshParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.ConceptGearMeshParametricStudyTool]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptGearMeshCompoundParametricStudyTool._Cast_ConceptGearMeshCompoundParametricStudyTool":
        return self._Cast_ConceptGearMeshCompoundParametricStudyTool(self)
