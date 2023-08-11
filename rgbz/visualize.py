import numpy as np
import matplotlib.pyplot as plt
from .core import float_to_rgb

def visualize_rgbz(data):
    """
    Visualizes the 2D elevation data in RGB format using matplotlib.

    Parameters:
    - data (numpy.array): 2D array with elevation data.
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

    # Display the image
    plt.imshow(rgb_image)
    plt.axis('off')  # Don't show axis values
    plt.show()

