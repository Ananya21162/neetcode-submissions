# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        temp1 = head
        temp2 = temp1.next
        temp3 = temp2.next
        temp1.next = None
        while temp3 != None:
            temp2.next = temp1
            temp1 = temp2
            temp2 = temp3
            temp3 = temp3.next
        temp2.next = temp1
        head = temp2
        return temp2