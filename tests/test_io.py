import unittest
import numpy as np
from rgbz.io import read_tiff, write_png

class TestIOFunctions(unittest.TestCase):

    def test_read_tiff(self):
        # Assuming you have a sample test TIFF file named 'test.tiff'
        data = read_tiff(r'data\1045225064950_202001_CLIP_DEM\1045225064950_202001_CLIP_DEM.tif')
        
        # Check the type and shape or any other property of the returned data
        self.assertIsInstance(data, np.ndarray)
        # Further checks can be added as per requirement
        
    
    def test_read_tiff_lzw(self):
        # Assuming you have a sample test TIFF file named 'test.tiff'
        data = read_tiff(r'data\1045225064950_202001_RAW_DEM\1045225064950_202001_RAW_DEM.tif')
        
        # Check the type and shape or any other property of the returned data
        self.assertIsInstance(data, np.ndarray)
        # Further checks can be added as per requirement
        
    def test_write_png(self):
        # Generate some dummy data
        dummy_data = np.random.randint(0, 256, (10, 10, 3), dtype=np.uint8)
        
        # Write this data to a PNG file
        write_png(dummy_data, 'test_output.png')
        
        # For this test, we're just ensuring the function runs without error.
        # Further verification can involve reading the PNG back and checking its content.

if __name__ == "__main__":
    unittest.main()
