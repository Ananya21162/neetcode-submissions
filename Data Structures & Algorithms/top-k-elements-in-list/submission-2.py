class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num,0)+1
        minHeap = []
        for key, value in freqMap.items():
            if len(minHeap) < k:
                heapq.heappush(minHeap,[value,key])
            else:
                if minHeap[0][0] < value:
                    heapq.heappop(minHeap)
                    heapq.heappush(minHeap,[value,key])
        ans = []
        for value in minHeap:
            ans.append(value[1])
        return ans
            
        