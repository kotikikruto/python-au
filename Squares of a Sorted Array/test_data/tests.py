import unittest
from solution import Solution


class TestSortedSquares(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortedSquares([]), [])

    def test_mixed_nums(self):
        result = self.solution.sortedSquares([-4, -1, 0, 3, 10])
        expected = [0, 1, 9, 16, 100]
        self.assertEqual(result, expected)

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortedSquares([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortedSquares([-5, -4, -3, -2, -1]), [1, 4, 9, 16, 25])
