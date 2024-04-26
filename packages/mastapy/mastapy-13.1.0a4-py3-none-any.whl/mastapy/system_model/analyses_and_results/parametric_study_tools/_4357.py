"""CouplingHalfParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4404
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2603
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4341,
        _4346,
        _4361,
        _4418,
        _4425,
        _4430,
        _4440,
        _4450,
        _4452,
        _4453,
        _4456,
        _4457,
        _4344,
        _4416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7571
    from mastapy.system_model.analyses_and_results import _2680, _2676, _2674


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingHalfParametricStudyTool")


class CouplingHalfParametricStudyTool(_4404.MountableComponentParametricStudyTool):
    """CouplingHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfParametricStudyTool")

    class _Cast_CouplingHalfParametricStudyTool:
        """Special nested class for casting CouplingHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            parent: "CouplingHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4404.MountableComponentParametricStudyTool":
            return self._parent._cast(_4404.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4344.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4344,
            )

            return self._parent._cast(_4344.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4416.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_7571.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7571

            return self._parent._cast(_7571.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2680.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2680

            return self._parent._cast(_2680.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2676.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2676

            return self._parent._cast(_2676.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2674.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2674

            return self._parent._cast(_2674.DesignEntityAnalysis)

        @property
        def clutch_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4341.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4346.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.ConceptCouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4361.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.CVTPulleyParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4418.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4418,
            )

            return self._parent._cast(
                _4418.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4425.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.PulleyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4430.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.RollingRingParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4440.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.SpringDamperHalfParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4450.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4450,
            )

            return self._parent._cast(_4450.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4452.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4452,
            )

            return self._parent._cast(_4452.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4453.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4453,
            )

            return self._parent._cast(_4453.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4456.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4456,
            )

            return self._parent._cast(_4456.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4457.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4457,
            )

            return self._parent._cast(_4457.TorqueConverterTurbineParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "CouplingHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2603.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool":
        return self._Cast_CouplingHalfParametricStudyTool(self)
