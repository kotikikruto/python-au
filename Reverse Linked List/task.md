## Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

[Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

<details><summary>Test cases</summary><blockquote>

```python
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        list = self.get_linked_list_values(head)
        list = list[::-1]
        list = self.create_single_linked_list(list)
        return list
```
