class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        ss = [-s for s in stones]
        heapq.heapify(ss)
        while len(ss) > 1:
            first = heapq.heappop(ss)
            second = heapq.heappop(ss)

            if first != second:
                heapq.heappush(ss,abs(first-second)*-1)
        ss.append(0)    
        return abs(ss[0])