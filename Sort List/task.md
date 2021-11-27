## Sort List

Given the head of a linked list, return the list after sorting it in ascending order.

[Sort List](https://leetcode.com/problems/sort-list/)

<details><summary>Test cases</summary><blockquote>

```python
import unittest
from solution import Solution


class TestSortList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_nums(self):
        self.assertEqual(self.solution.sortList([]), [])

    def test_mixed_nums(self):
        self.assertEqual(self.solution.sortList([1, -5, 0, 4]), [-5, 0, 1, 4])

    def test_positive_nums(self):
        self.assertEqual(self.solution.sortList([4, 2, 3, 1]), [1, 2, 3, 4])

    def test_negative_nums(self):
        self.assertEqual(self.solution.sortList([-2, -1, -3, -4]), [-4, -3, -2, -1])
```
</blockquote></details>

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_linked_list_values(self, head):
        result = []
        cur = head
        while cur != None:
            result.append(cur.val)
            cur = cur.next
        return result

    def create_single_linked_list(self, values):
        previous_node = ListNode(values[len(values) - 1])
        for i in range(0, len(values) - 1):
            next_node = ListNode(values[len(values) - i - 2], previous_node)
            previous_node = next_node
        return previous_node

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        list = self.get_linked_list_values(head)
        list = sorted(list)
        list = self.create_single_linked_list(list)
        return list
```
