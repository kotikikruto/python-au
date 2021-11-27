import unittest
from solution import Solution


class TestIntersectionOfTwoLinkedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_heads(self):
        self.assertEqual(self.solution.getIntersectionNode([], []), None)

    def test_exists_intersection(self):
        self.assertEqual(self.solution.getIntersectionNode([4, 8, 4, 5], [5, 6, 8, 4, 5]), 8)

    def test_no_exists_intersection(self):
        self.assertEqual(self.solution.getIntersectionNode([2, 6, 4], [1, 5]), None)