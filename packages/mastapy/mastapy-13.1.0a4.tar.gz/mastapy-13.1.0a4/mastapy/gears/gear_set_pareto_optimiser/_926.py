"""MicroGeometryDesignSpaceSearchStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility.optimisation import _1552
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_set_pareto_optimiser import _928, _929
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryDesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="MicroGeometryDesignSpaceSearchStrategyDatabase")


class MicroGeometryDesignSpaceSearchStrategyDatabase(
    _1552.DesignSpaceSearchStrategyDatabase
):
    """MicroGeometryDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryDesignSpaceSearchStrategyDatabase"
    )

    class _Cast_MicroGeometryDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
            parent: "MicroGeometryDesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def design_space_search_strategy_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_1843.NamedDatabase":
            pass

            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_928.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "_929.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
        ) -> "MicroGeometryDesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase",
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
        self: Self,
        instance_to_wrap: "MicroGeometryDesignSpaceSearchStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase":
        return self._Cast_MicroGeometryDesignSpaceSearchStrategyDatabase(self)
