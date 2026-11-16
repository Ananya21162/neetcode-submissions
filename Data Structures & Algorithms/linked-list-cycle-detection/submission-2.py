# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        while fast:
            slow = slow.next
            if fast.next == None:
                return False
            elif fast.next.next == None:
                return False
            else:
                fast = fast.next.next
            if fast.next == slow.next:
                return True
        return False
