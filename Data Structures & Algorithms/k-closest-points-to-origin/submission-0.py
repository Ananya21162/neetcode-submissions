class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        dist_map = defaultdict(list)
        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x*x + y*y)
            if dist not in dist_map:
                dist_map[dist] = [point]
            else:
                dist_map[dist].append(point)
        dist = list(dist_map.keys())
        heapq.heapify(dist)
        i = 0
        while i < k:
            for p in dist_map[heapq.heappop(dist)]:
                ans.append(p)
                i += 1
                
        return ans