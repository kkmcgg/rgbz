"""
io.py - I/O functionalities for the RGBZ library.

This module provides functions for reading elevation data from TIFF files 
and writing them as RGB values to PNG files.
"""

import numpy as np
from tifffile import imread
from PIL import Image

def read_tiff(tiff_path):
    """
    Read a TIFF file and return its data as a numpy array.

    Parameters:
    - tiff_path (str): Path to the TIFF file.

    Returns:
    - data (numpy.array): Data from the TIFF file.
    """
    return imread(tiff_path)

def write_png(data, png_path):
    """
    Write a numpy array with RGB or RGBA data to a PNG file.

    Parameters:
    - data (numpy.array): RGB or RGBA data.
    - png_path (str): Path where the PNG file should be saved.
    """

    # Check if the data is either RGB or RGBA
    if data.shape[-1] not in [3, 4]:
        raise ValueError("Input data must be RGB or RGBA format")

    # Use Pillow to save the RGB or RGBA image as PNG
    im = Image.fromarray(data)
    im.save(png_path)
