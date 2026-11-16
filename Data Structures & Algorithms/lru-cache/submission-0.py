class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(-1,-1)
        self.right = Node(-1,-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.cache = {} # key as key and value as Node
    def remove(self,node):
        pre, nextNode = node.prev, node.next
        pre.next = nextNode
        nextNode.prev = pre
        del node
    def insert(self,node):
        pre = self.right.prev
        pre.next,node.prev = node, pre
        node.next = self.right
        self.right.prev = node

        
    def get(self, key: int) -> int:
        if key in self.cache:
            # update node to rightmost
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # delete the older node and insert new one at end
            self.remove(self.cache[key])
            self.cache[key] = Node(key,value)
            self.insert(self.cache[key])
        else:
            new = Node(key,value)
            self.insert(new)
            self.cache[key] = new
            if len(self.cache) > self.capacity:
                # evict the leftmost
                del self.cache[self.left.next.key]
                self.remove(self.left.next)



