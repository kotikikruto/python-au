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