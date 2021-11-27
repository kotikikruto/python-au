## Intersection of Two Linked Lists

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

[Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)

<details><summary>Test cases</summary><blockquote>

```python
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
```   
</blockquote></details>

```python
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        seen = set()
        itr = headA
        while itr:
            seen.add(itr)
            itr = itr.next
        itr = headB
        while itr:
            if seen.__contains__(itr):
                return itr
            itr = itr.next
        return None
```
