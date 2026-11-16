class MinStack:

    def __init__(self):
        self.stack = []
        self.minHeap = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.minHeap,val)

    def pop(self) -> None:
        for i in range(len(self.minHeap)):
            if self.minHeap[i] == self.stack[-1]:
                break
        self.minHeap[i], self.minHeap[-1] = self.minHeap[-1],self.minHeap[i]
        self.minHeap.pop()
        heapq.heapify(self.minHeap)
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minHeap[0]
        
