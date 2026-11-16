class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key= lambda x: x[0])
        i, n = 1, len(intervals)
        while i < n+1:
            o_start , o_end= intervals[i-1][0], intervals[i-1][1]
            while i < n and o_start <= intervals[i][0] <= o_end:
                o_start = min(o_start,intervals[i][0])
                o_end = max(o_end,intervals[i][1])
                i += 1
            res.append([o_start,o_end])
            i += 1
        return res