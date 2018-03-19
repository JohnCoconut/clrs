import unittest
from random import shuffle
from two_sum import two_sum
from two_sum import merge_sort
from timeit import timeit

class test_sort(unittest.TestCase):

    def test_merge_sort(self):
        size = 100000000
        li = list(range(size))
        shuffle(li)
        t = timeit(lambda: merge_sort(li, 0, len(li)-1), number=1)
        print("time spend on merge sort is: ", str(t))
        self.assertEqual(sorted(li), li)

    def test_two_sum(self):
        li = [3, 1, 4, 1, 5, 9, 2, 6]
        merge_sort(li, 0, len(li)-1)
        self.assertEqual(two_sum(li, 12), (3, 7))


if __name__ == "__main__":
    unittest.main()
