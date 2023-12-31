import numpy as np

def clamp(array,min_val,max_val):
    '''returns an array clamped between min and max'''
    return np.clip(array, min_val, max_val)

def normalize(array):
    ''' returns an array normalized from 0 to 1 '''
    min_val = np.min(array)
    max_val = np.max(array)
    return (array - min_val) / (max_val - min_val)

def rgb_like(input_array, bit_depth=8, channels=3):
    """
    Create an empty RGB or RGBA array with the shape of the input 2D array.

    Parameters:
    - input_array (numpy.ndarray): The input 2D array.
    - bit_depth (int): Depth of the new array (8 or 16 bits).
    - channels (int): Number of channels (3 for RGB, 4 for RGBA).

    Returns:
    - numpy.ndarray: An empty RGB or RGBA array.
    """
    
    if bit_depth == 8:
        dtype = np.uint8
    elif bit_depth == 16:
        dtype = np.uint16
    else:
        raise ValueError("bit_depth should be 8 or 16")
    
    if channels not in [3, 4]:
        raise ValueError("channels should be 3 (RGB) or 4 (RGBA)")
    
    # Determine the new shape
    new_shape = (*input_array.shape, channels)

    return np.empty(new_shape, dtype=dtype)

def hsv_to_rgb(h, s, v):
    h = h * 2
    s = s / 255.0
    v = v / 255.0
    
    i = (h / 60).astype(np.int) % 6
    f = (h / 60) - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    r = np.zeros_like(h)
    g = np.zeros_like(h)
    b = np.zeros_like(h)

    mask = i == 0
    r[mask], g[mask], b[mask] = v[mask], t[mask], p[mask]

    mask = i == 1
    r[mask], g[mask], b[mask] = q[mask], v[mask], p[mask]

    mask = i == 2
    r[mask], g[mask], b[mask] = p[mask], v[mask], t[mask]

    mask = i == 3
    r[mask], g[mask], b[mask] = p[mask], q[mask], v[mask]

    mask = i == 4
    r[mask], g[mask], b[mask] = t[mask], p[mask], v[mask]

    mask = i == 5
    r[mask], g[mask], b[mask] = v[mask], p[mask], q[mask]

    return (r * 255).astype(np.int), (g * 255).astype(np.int), (b * 255).astype(np.int)

if __name__=='__main__':
    # Example usage
    h = np.array([10, 50])
    s = np.array([128, 200])
    v = np.array([200, 150])
    r, g, b = hsv_to_rgb(h, s, v)
    print(f"RGB: {list(zip(r, g, b))}")
