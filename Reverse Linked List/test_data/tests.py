import unittest
from solution import Solution


class TestReverseLinked_List(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.reverseList([]), [])

    def test_non_empty_list(self):
        self.assertEqual(self.solution.reverseList([0, 2, 4]), [4, 2, 0])

    def test_non_empty_list_1(self):
        self.assertEqual(self.solution.reverseList([1]), [1])