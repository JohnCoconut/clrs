import unittest
from timeit import timeit
from random import shuffle
from merge_sort import merge_sort
from merge_sort2 import merge_sort2
from merge_sort2 import insertion_sort

class test_sort(unittest.TestCase):

    def test_merge_sort(self):
        size = 1000000
        l = list(range(size))
        _l = l[:]
        shuffle(l)
        l2 = l[:]
        t1 = timeit(lambda: merge_sort2(l, 0, len(l)-1), number=1)
        merge_sort(l, 0, size-1)
        print("Time to sort with mergesort: " + str(t1))
#        t2 = timeit(lambda: insertion_sort(l2, 0, len(l2)-1), number=1)
#        print("Time to sort with insertionsort: " + str(t2))
        self.assertEqual(_l, l)
#        self.assertEqual(_l, l2)

if __name__ == "__main__":
    unittest.main()
