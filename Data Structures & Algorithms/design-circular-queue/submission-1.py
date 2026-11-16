class Node:
    def __init__(self,val = 0):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = Node(-1)
        self.rear = self.front
        self.space = k
  

    def enQueue(self, value: int) -> bool:
        # add elements in the queue
        if self.isFull():
            return False
        temp = Node(val = value)
        self.rear.next = temp
        self.rear = self.rear.next
        self.space -= 1
        return True
    
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front.next = self.front.next.next
        if not self.front.next:
            self.rear = self.front
        self.space += 1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.front.next.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.rear.val
        return -1

    def isEmpty(self) -> bool:
        if self.front.next is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.space == 0:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()