import unittest
from bubble_sort import bubble
import random
import copy


class TestStringMethods(unittest.TestCase):
    def test_bubblesort(self):
        data = [5, 9, 6, 1, 3, 2, 7, 4, 8]
        data = bubble(data)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], bubble(data))
        self.assertEqual([], bubble([]))
        self.assertEqual(data, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_bubblesort_big(self):
        data = list(range(100))
        self.assertEqual(data, bubble(data))

        data = list(range(99, -1, -1))
        self.assertEqual(data, bubble(data))

    def test_random(self):
        data1 = random.sample(range(0, 100), 30)
        data2 = copy.deepcopy(data1)
        bubble(data1)
        data2.sort()
        self.assertEqual(data2, data1)


if __name__ == "__main__":
    unittest.main()
