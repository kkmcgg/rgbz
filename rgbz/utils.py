import numpy as np

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

# Example usage
h = np.array([10, 50])
s = np.array([128, 200])
v = np.array([200, 150])
r, g, b = hsv_to_rgb(h, s, v)
print(f"RGB: {list(zip(r, g, b))}")
