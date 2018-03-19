import unittest
from random import shuffle
from max_subarray import max_subarray
from max_subarray2 import max_subarray2
from max_subarray3 import max_subarray3

class TestMaxSubArray(unittest.TestCase):

    def testMaxSubArray(self):
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        length = len(a)
        actual = max_subarray(a, 0, length - 1)
        expected = (7, 10, 43)
        self.assertEqual(actual, expected)
        
    def testEmptyArray(self):
        a = []
        length = len(a)
        actual = max_subarray(a, 0, length - 1)
        expected = (7, 10, 43)
        self.assertEqual(actual, expected)

    def testMaxSubArray2(self):
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        length = len(a)
        actual = max_subarray2(a)
        expected = (7, 10, 43)
        self.assertEqual(actual, expected)

    def testMaxSubArra3(self):
        a = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
        length = len(a)
        actual = max_subarray3(a)
        expected = (7, 10, 43)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
