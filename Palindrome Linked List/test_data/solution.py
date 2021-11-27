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

