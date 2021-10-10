# Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

[Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

<details><summary>Test cases</summary><blockquote>

```python
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
        self.assertEqual(self.solution.sortedSquares([-10, -5, -2]), [4, 25, 100])

    def test_find_with_positive(self):
        self.assertEqual(self.solution.get_first_non_negative([2, 3, 5]), 0)

    def test_find_with_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, -2]), 3)

    def test_find_with_non_negative(self):
        self.assertEqual(self.solution.get_first_non_negative([0, 1, 2, 3]), 0)

    def test_find_with_mixed(self):
        self.assertEqual(self.solution.get_first_non_negative([-10, -5, 0, 1, 2, 3]), 2)
```
</blockquote></details>

```python
from typing import List


class Solution:
    def merge(self, fl, sl):
        f = 0
        s = 0
        result = []
        while f < len(fl) and s < len(sl):
            if fl[f] < sl[s]:
                result.append(fl[f])
                f += 1
            else:
                result.append(sl[s])
                s += 1
        while f < len(fl):
            result.append(fl[f])
            f += 1
        while s < len(sl):
            result.append(sl[s])
            s += 1
        return result

    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst1 = []
        lst2 = []
        i = 0
        while i < len(nums) and nums[i] < 0:
            lst1.append(nums[i])
            i += 1
        while i < len(nums):
            lst2.append(nums[i])
            i += 1
        lst11 = []
        lst22 = []
        for j in range(len(lst1)):
            lst11.append(lst1[len(lst1) - j - 1] ** 2)
        for j in range(len(lst2)):
            lst22.append(lst2[j] ** 2)
        return self.merge(lst11, lst22)
```
