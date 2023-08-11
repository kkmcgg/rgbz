import unittest
import numpy as np
from rgbz.core import method1_encode,method1_decode

class TestIOFunctions(unittest.TestCase):
    
    def test_method1_encode(self):
        data = dummy_data = np.random.random((10, 10)) 
        rgb_array = method1_encode(dummy_data)
        self.assertIsNotNone(rgb_array) 

    def test_method1_decode(self):
        pass

if __name__ == "__main__":
    unittest.main()

    # note, run with PS C:\_dev\rgbz> python -m tests.test_core
