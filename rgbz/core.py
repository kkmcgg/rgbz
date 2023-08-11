
import numpy as np
from .constants import MAX_ELEVATION, MIN_ELEVATION
from .utils import clamp, normalize, hsv_to_rgb, rgb_like
from .io import read_tiff

def method1_encode(z_array, m=MIN_ELEVATION, M = MAX_ELEVATION):

  z_array = clamp(z_array,m,M)
  z_array = normalize(z_array)
  z_array = z_array * 2**24

  r_array = np.floor((z_array / 2**16)%256)
  g_array = np.floor((z_array / 2**8)%256)
  b_array = np.floor((z_array / 2**0)%256)
  
  rgb_array = rgb_like(z_array)

  rgb_array[:, :, 0] = r_array
  rgb_array[:, :, 1] = g_array
  rgb_array[:, :, 2] = b_array


  return rgb_array
def method1_decode(rgb_array):

  z_array = None

  return z_array

if __name__ == '__main__':
  #mucking about
  if 0:
    print('hello')
    dummy_data = np.random.random((10, 10)) 
    # dummy_data = np.random.random((256, 256))
    rgb_array = method1_encode(dummy_data)
    import matplotlib.pyplot as plt
    plt.imshow(dummy_data, cmap='gray')
    plt.show()
    plt.imshow(rgb_array)
    plt.show()

    from .io import write_png

    write_png(rgb_array,'test.png')

    # note run with PS C:\_dev\rgbz> python -m rgbz.core
  if 1:
    test_dem = r'data\1045225064950_202001_CLIP_DEM\1045225064950_202001_CLIP_DEM.tif'
    data = read_tiff(test_dem)
    rgb_array = method1_encode(data)
    import matplotlib.pyplot as plt
    plt.imshow(data, cmap='gray',vmin=MIN_ELEVATION, vmax = MAX_ELEVATION)
    plt.show()
    plt.imshow(rgb_array)
    plt.show()

