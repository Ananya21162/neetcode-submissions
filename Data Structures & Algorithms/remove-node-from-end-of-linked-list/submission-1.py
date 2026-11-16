# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        temp = head
        while temp:
            temp = temp.next
            N += 1
        count = N-n
        temp = head
        while count >1:
            temp = temp.next
            count -= 1
        # remove temp.next
        if N == n:
            head = head.next
            del temp
        else:
            if temp.next:
                node = temp.next
                temp.next = temp.next.next
                del node
        return head