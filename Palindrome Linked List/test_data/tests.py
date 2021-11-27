import unittest
from solution import Solution


class TestPalindromeLinkedList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.isPalindrome([]), True)

    def test_palindrome(self):
        self.assertEqual(self.solution.isPalindrome([1, 2, 1]), True)

    def test_non_palindrome(self):
        self.assertEqual(self.solution.isPalindrome([4, 2, 3, 1]), False)
