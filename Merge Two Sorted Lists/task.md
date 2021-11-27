## Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

[Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)

<details><summary>Test cases</summary><blockquote>

```python
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

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = self.get_linked_list_values(list1)
        list2 = self.get_linked_list_values(list2)
        if len(list1) == 0:
            if len(list2) == 0:
                return None
            return self.create_single_linked_list(list2)
        if len(list2) == 0:
            return self.create_single_linked_list(list1)

        a, b = 0, 0
        merged_list = []
        while True:
            if (a < len(list1)) and (b < len(list2)):
                if list1[a] < list2[b]:
                    merged_list.append(list1[a])
                    a += 1
                else:
                    merged_list.append(list2[b])
                    b += 1
            if a == len(list1):
                while b < len(list2):
                    merged_list.append(list2[b])
                    b += 1
                break
            if b == len(list2):
                while a < len(list1):
                    merged_list.append(list1[a])
                    a += 1
                break
        merged_list = self.create_single_linked_list(merged_list)
        return merged_list

```
