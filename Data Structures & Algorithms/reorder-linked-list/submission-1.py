# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head:
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            # reverse list starting from slow to end
            temp1, temp2 = slow, slow.next
            slow.next = None
            while temp2 and temp2.next:
                tmp = temp2.next
                temp2.next = temp1
                temp1 = temp2
                temp2 = tmp
            if temp2: 
                temp2.next = temp1
                h1, h2 = head, head.next
                e1, e2 = temp2,temp2.next
                while h2 and e2 :
                    h1.next = e1
                    e1.next = h2
                    h1, e1 = h2, e2
                    h2, e2 = h2.next, e2.next
            


            # return dummy.next