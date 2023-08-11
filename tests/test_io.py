import unittest
import numpy as np
from rgbz.io import read_tiff, write_png

class TestIOFunctions(unittest.TestCase):
    
    def test_read_tiff(self):
        # Assuming you have a sample test TIFF file named 'test.tiff'
        data = read_tiff('path_to_test_files/test.tiff')
        
        # Check the type and shape or any other property of the returned data
        self.assertIsInstance(data, np.ndarray)
        # Further checks can be added as per requirement
        
    def test_write_png(self):
        # Generate some dummy data
        dummy_data = np.random.random((10, 10))
        
        # Write this data to a PNG file
        write_png(dummy_data, 'path_to_test_files/test_output.png')
        
        # For this test, we're just ensuring the function runs without error.
        # Further verification can involve reading the PNG back and checking its content.

if __name__ == "__main__":
    unittest.main()
