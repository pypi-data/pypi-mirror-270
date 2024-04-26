"""SplineDampingOptions"""

from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy.math_utility.hertzian_contact import _1585
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import overridable_enum_runtime, conversion, constructor
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPLINE_DAMPING_OPTIONS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses", "SplineDampingOptions"
)


__docformat__ = "restructuredtext en"
__all__ = ("SplineDampingOptions",)


Self = TypeVar("Self", bound="SplineDampingOptions")


class SplineDampingOptions(_0.APIBase):
    """SplineDampingOptions

    This is a mastapy class.
    """

    TYPE = _SPLINE_DAMPING_OPTIONS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SplineDampingOptions")

    class _Cast_SplineDampingOptions:
        """Special nested class for casting SplineDampingOptions to subclasses."""

        def __init__(
            self: "SplineDampingOptions._Cast_SplineDampingOptions",
            parent: "SplineDampingOptions",
        ):
            self._parent = parent

        @property
        def spline_damping_options(
            self: "SplineDampingOptions._Cast_SplineDampingOptions",
        ) -> "SplineDampingOptions":
            return self._parent

        def __getattr__(
            self: "SplineDampingOptions._Cast_SplineDampingOptions", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SplineDampingOptions.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_damping_model(
        self: Self,
    ) -> "overridable.Overridable_ContactDampingModel":
        """Overridable[mastapy.math_utility.hertzian_contact.ContactDampingModel]"""
        temp = self.wrapped.ContactDampingModel

        if temp is None:
            return None

        value = overridable.Overridable_ContactDampingModel.wrapped_type()
        return overridable_enum_runtime.create(temp, value)

    @contact_damping_model.setter
    @enforce_parameter_types
    def contact_damping_model(
        self: Self,
        value: "Union[_1585.ContactDampingModel, Tuple[_1585.ContactDampingModel, bool]]",
    ):
        wrapper_type = overridable.Overridable_ContactDampingModel.wrapper_type()
        enclosed_type = overridable.Overridable_ContactDampingModel.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value, enclosed_type)
        value = wrapper_type[enclosed_type](
            value if value is not None else None, is_overridden
        )
        self.wrapped.ContactDampingModel = value

    @property
    def damping_factor(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.DampingFactor

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @damping_factor.setter
    @enforce_parameter_types
    def damping_factor(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.DampingFactor = value

    @property
    def penetration_for_max_damping(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.PenetrationForMaxDamping

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @penetration_for_max_damping.setter
    @enforce_parameter_types
    def penetration_for_max_damping(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.PenetrationForMaxDamping = value

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def cast_to(self: Self) -> "SplineDampingOptions._Cast_SplineDampingOptions":
        return self._Cast_SplineDampingOptions(self)
