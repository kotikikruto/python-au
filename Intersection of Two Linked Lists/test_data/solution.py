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