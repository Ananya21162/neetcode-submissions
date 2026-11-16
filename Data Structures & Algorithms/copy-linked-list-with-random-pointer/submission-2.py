"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        list_map = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            list_map[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = list_map[curr]
            if curr.next:
                copy.next = list_map[curr.next]
            if curr.random:
                copy.random = list_map[curr.random]
            curr = curr.next
        return list_map[head]
