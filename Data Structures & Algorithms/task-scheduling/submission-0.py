class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        freqMap = {}
        for task in tasks:
            if task not in freqMap:
                freqMap[task] = 1
            else:
                freqMap[task] += 1
        freq = [-t for t in freqMap.values()]
        heapq.heapify(freq)
        q = deque()
        while len(freq)>0 or len(q)>0:
            time += 1
            
            if len(freq) == 0:
                time = q[0][1]
            else:

                item = heapq.heappop(freq)
                if item+1 < 0:
                    q.append([item+1,n+time])
                
            if q and q[0][1] == time:
                v = q.popleft()
                heapq.heappush(freq,v[0])
        return time