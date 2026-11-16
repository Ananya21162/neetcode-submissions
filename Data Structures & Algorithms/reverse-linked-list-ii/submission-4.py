# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 0
        if not head or left == right:
            return head
        temp = head
        prev = None
        leftP, rightP = head, head
        while temp:
            count += 1
            if left-count == 1:
                prev = temp
            if left == count:
                leftP = temp
            if right == count:
                rightP = temp
                break
            
            temp = temp.next
        rightP2 = rightP.next
        leftP2 = leftP.next
        leftTP = leftP
        while leftTP != rightP: # condition
            tmp = leftP2.next
            leftP2.next = leftTP
            leftTP = leftP2
            leftP2 = tmp
        leftP.next = rightP2
        if prev:
            prev.next = rightP
            return head
        return rightP
