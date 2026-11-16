class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        res = []
        pending, available = [], []
        for i in range(len(tasks)):
            heapq.heappush(pending,[tasks[i][0],tasks[i][1],i])
        time = 0
        while pending or available:
            while pending and pending[0][0] <= time:
                enq, process, i = heapq.heappop(pending)
                heapq.heappush(available, [process,i])
            
            if not available:
                time = pending[0][0]
                continue
            
            processingT, i = heapq.heappop(available)
            time += processingT
            res.append(i)
        return res