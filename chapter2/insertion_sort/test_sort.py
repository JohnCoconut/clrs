import unittest
from random import shuffle
from insertion_sort_recursive import insertion_sort

class test_sort(unittest.TestCase):

    def test_insertion(self):
        li = list(range(900))
        shuffle(li)
        self.assertTrue(sorted(li), insertion_sort(li, len(li)-1))


if __name__ == "__main__":
    unittest.main()
