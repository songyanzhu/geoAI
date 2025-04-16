import os
from pathlib import Path
from . import functions as gfuncs

__all__ = ["gfuncs", "data_path"]

data_path = Path(__file__).parent.joinpath('data')