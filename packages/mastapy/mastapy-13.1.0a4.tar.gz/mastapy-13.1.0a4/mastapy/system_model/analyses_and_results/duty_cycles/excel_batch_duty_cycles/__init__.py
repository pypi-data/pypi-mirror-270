"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._6563 import ExcelBatchDutyCycleCreator
    from ._6564 import ExcelBatchDutyCycleSpectraCreatorDetails
    from ._6565 import ExcelFileDetails
    from ._6566 import ExcelSheet
    from ._6567 import ExcelSheetDesignStateSelector
    from ._6568 import MASTAFileDetails
else:
    import_structure = {
        "_6563": ["ExcelBatchDutyCycleCreator"],
        "_6564": ["ExcelBatchDutyCycleSpectraCreatorDetails"],
        "_6565": ["ExcelFileDetails"],
        "_6566": ["ExcelSheet"],
        "_6567": ["ExcelSheetDesignStateSelector"],
        "_6568": ["MASTAFileDetails"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "ExcelBatchDutyCycleCreator",
    "ExcelBatchDutyCycleSpectraCreatorDetails",
    "ExcelFileDetails",
    "ExcelSheet",
    "ExcelSheetDesignStateSelector",
    "MASTAFileDetails",
)
