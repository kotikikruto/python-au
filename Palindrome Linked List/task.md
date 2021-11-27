## Palindrome Linked List

Given the head of a singly linked list, return true if it is a palindrome.

[Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

<details><summary>Test cases</summary><blockquote>

```python
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list = self.get_linked_list_values(head)
        for i in range(len(list)//2):
            if list[i] != list[len(list)-i-1]:
                return False
        return True


```
