import os
from . import functions as gfuncs

__all__ = ["gfuncs", "test_path"]

_module_path = os.path.dirname(__file__)

test_path = _module_path