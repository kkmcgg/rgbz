"""
io.py - I/O functionalities for the RGBZ library.

This module provides functions for reading elevation data from TIFF files 
and writing them as RGB values to PNG files.
"""

import numpy as np
from tifffile import imread
from PIL import Image
from .core import float_to_rgb # not implemeted

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
    Write a numpy array with elevation data to a PNG file as RGB values.

    Parameters:
    - data (numpy.array): Elevation data.
    - png_path (str): Path where the PNG file should be saved.
    """
    # Assuming data is a 2D array where each element is a 24-bit float
    # representing elevation that we want to convert to an RGB value

    # Get the shape of the data
    height, width = data.shape

    # Create an empty 3D array to store RGB values
    rgb_image = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            r, g, b = float_to_rgb(data[i, j]) 
            rgb_image[i, j] = [r, g, b]

    # Use Pillow to save the RGB image as PNG
    im = Image.fromarray(rgb_image)
    im.save(png_path)

