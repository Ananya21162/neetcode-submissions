from collections import defaultdict

class DLLNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class ListNode:
    def __init__(self):
        self.left = DLLNode(-1)
        self.right = DLLNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.map = {}

    def length(self):
        return len(self.map)

    def insert(self, key):
        if key in self.map:
            self.remove(key)
        node = DLLNode(key)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.map[key] = node

    def remove(self, key):
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.map[key]

    def popleft(self):
        node = self.left.next
        if node == self.right:
            return None
        self.remove(node.key)
        return node.key


class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.valueMap = {}
        self.freq = defaultdict(ListNode)
        self.cnt = {}
        self.lfuCnt = 0

    def get(self, key: int) -> int:
        if key not in self.valueMap:
            return -1

        f = self.cnt[key]
        self.freq[f].remove(key)

        if f == self.lfuCnt and self.freq[f].length() == 0:
            self.lfuCnt += 1

        self.cnt[key] += 1
        self.freq[self.cnt[key]].insert(key)
        return self.valueMap[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.valueMap:
            self.valueMap[key] = value
            self.get(key)
            return

        if len(self.valueMap) == self.cap:
            evict = self.freq[self.lfuCnt].popleft()
            del self.valueMap[evict]
            del self.cnt[evict]

        self.valueMap[key] = value
        self.cnt[key] = 1
        self.freq[1].insert(key)
        self.lfuCnt = 1
