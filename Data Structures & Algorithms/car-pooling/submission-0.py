class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        minHeap = []
        trips.sort(key = lambda x : x[1] )
        countPassenger = 0
        for trip in trips:
            while minHeap and minHeap[0][0] <= trip[1]:
                value = heapq.heappop(minHeap) # end time , numP
                countPassenger -= value[1]
            countPassenger += trip[0]
            if countPassenger > capacity:
                return False
            heapq.heappush(minHeap,[trip[2],trip[0]])
        return True