class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = {}
        for i in range(len(s)):
            if s[i] not in freqMap:
                freqMap[s[i]] = 1
            else:
                freqMap[s[i]] += 1
        minHeap = []
        for key, value in freqMap.items():
            heapq.heappush(minHeap,[-value,key])
        q = deque()
        t = 0
        ans = ""
        while q or minHeap:
            t += 1
            if minHeap:
                value = heapq.heappop(minHeap)
                ans += value[1]
                if value[0]+1 < 0:
                    q.append((t+1,value[0]+1,value[1]))
            if q and q[0][0] <= t:
                new = q.popleft()
                heapq.heappush(minHeap, [new[1],new[2]])
            else:
                if not minHeap and len(q) < 2:
                    break
        return ans if len(ans) == len(s) else ""

