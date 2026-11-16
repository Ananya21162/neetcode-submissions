class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minHeap:
            minV = min(val, self.minHeap[-1])
            self.minHeap.append(minV)
        else:
            self.minHeap.append(val)


    def pop(self) -> None:
        self.minHeap.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[-1]
        
