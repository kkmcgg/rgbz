"""
RGBZ - A Python package for manipulating and working with RGBZ color data.

Author: Kevin Kirkaldy McGuigan
License: MIT
"""

# Import main functionalities for easier access to end users
from .core import *
from .io import read_rgbz_file, write_rgbz_file
from .visualizer import visualize_rgbz

# Define package-wide constants (if they exist in constants.py)
from .constants import MAX_VALUE, MIN_VALUE

# Optionally, if you have custom exceptions you want users to access easily
from .exceptions import RGBZError, RGBZValueError

# Define what gets imported with "from rgbz import *"
__all__ = [
    "RGBZColor", 
    "some_rgbz_function",
    "read_rgbz_file",
    "write_rgbz_file",
    "visualize_rgbz",
    "MAX_VALUE",
    "MIN_VALUE",
    "RGBZError",
    "RGBZValueError"
]

# Define package's version number
__version__ = "0.1.0"
