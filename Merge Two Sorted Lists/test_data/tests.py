import unittest
from solution import Solution


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([], []), [])

    def test_one_empty_list(self):
        self.assertEqual(self.solution.mergeTwoLists([2], []), [2])

    def test_two_mixed_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([1, 5], [-3, 2, 7]), [-3, 1, 2, 5, 7])

    def test_positive_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([2], [1, 3, 4]), [1, 2, 3, 4])

    def test_negative_lists(self):
        self.assertEqual(self.solution.mergeTwoLists([-1], [-4, -3, -2]), [-4, -3, -2, -1])
