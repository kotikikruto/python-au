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
