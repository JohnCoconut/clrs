import unittest
from binary_search import binary_search

class test_search(unittest.TestCase):

    def test_search(self):
        a = list(range(10000))
        for i in a:
            self.assertEqual(binary_search(a, 0, len(a) - 1, i), a.index(i))

if __name__ == "__main__":
    unittest.main()
