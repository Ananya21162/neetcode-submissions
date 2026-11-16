class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        for i in range(len(arr)):
            diff = -1*abs(arr[i]-x)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (diff,arr[i]))
            else:
                if diff > maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,(diff,arr[i]))
        ans = []
        for item in maxHeap:
            ans.append(item[1])
        ans.sort()
        return ans