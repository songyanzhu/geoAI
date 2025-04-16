import os
from pathlib import Path
from . import functions as gfuncs

__all__ = ["gfuncs", "data_path"]

# _module_path = os.path.dirname(__file__)

# test_path = _module_path

data_path = Path(__file__).parent.joinpath('data')