import unittest
from solution import Solution


class TestMiddleOfTheLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.middleNode([]), [])

    def test_even_len_list(self):
        self.assertEqual(self.solution.middleNode([1, 2]), [2])

    def test_uneven_len_list(self):
        self.assertEqual(self.solution.middleNode([1, 2, 3]), [2, 3])
