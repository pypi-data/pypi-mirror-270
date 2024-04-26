"""MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_set_pareto_optimiser import _926
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.GearSetParetoOptimiser",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
)

if TYPE_CHECKING:
    from mastapy.math_utility.optimisation import _1552
    from mastapy.utility.databases import _1843, _1846, _1839


__docformat__ = "restructuredtext en"
__all__ = ("MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",)


Self = TypeVar("Self", bound="MicroGeometryGearSetDesignSpaceSearchStrategyDatabase")


class MicroGeometryGearSetDesignSpaceSearchStrategyDatabase(
    _926.MicroGeometryDesignSpaceSearchStrategyDatabase
):
    """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_GEAR_SET_DESIGN_SPACE_SEARCH_STRATEGY_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"
    )

    class _Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase:
        """Special nested class for casting MicroGeometryGearSetDesignSpaceSearchStrategyDatabase to subclasses."""

        def __init__(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
            parent: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ):
            self._parent = parent

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "_926.MicroGeometryDesignSpaceSearchStrategyDatabase":
            return self._parent._cast(
                _926.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "_1552.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1552

            return self._parent._cast(_1552.DesignSpaceSearchStrategyDatabase)

        @property
        def named_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "_1843.NamedDatabase":
            pass

            from mastapy.utility.databases import _1843

            return self._parent._cast(_1843.NamedDatabase)

        @property
        def sql_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "_1846.SQLDatabase":
            pass

            from mastapy.utility.databases import _1846

            return self._parent._cast(_1846.SQLDatabase)

        @property
        def database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "_1839.Database":
            pass

            from mastapy.utility.databases import _1839

            return self._parent._cast(_1839.Database)

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
        ) -> "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            return self._parent

        def __getattr__(
            self: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
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
        instance_to_wrap: "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
        return self._Cast_MicroGeometryGearSetDesignSpaceSearchStrategyDatabase(self)
