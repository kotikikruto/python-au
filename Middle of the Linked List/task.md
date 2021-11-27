## Middle of the Linked List

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

[Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

<details><summary>Test cases</summary><blockquote>

```python
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

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        list = self.get_linked_list_values(head)
        val = []
        for i in range(len(list) // 2, len(list)):
            val.append(list[i])

        return self.create_single_linked_list(val)
```
