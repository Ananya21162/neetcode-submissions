"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def exists(self,bucket, interval):
        # checks if interval exists/ overlaps in the bucket intervals
        # use binary search
        # boolean function
        l, r = 0, len(bucket)-1
        start, end = interval.start, interval.end
        while l <= r:
            mid = (l+r) // 2
            if (bucket[mid].start <= start  and start < bucket[mid].end) or (bucket[mid].start < end and end <= bucket[mid].end):
                return True
            elif bucket[mid].end < start:
                l = mid +1
            else:
                r = mid-1
        return False
    def findbucket(self,interval,buckets):
        for bucket in buckets:
            # do binary search for interval:
            if self.exists(bucket, interval):
                continue
            else:
                bucket.append(interval)
                return True
        return False
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)== 0:
            return 0
        buckets = []
        intervals.sort(key = lambda x: x.start)

        prevStart, prevEnd = intervals[0].start, intervals[0].end
        day = 1
        for i in range(1, len(intervals)):
            # check for overlap
            if prevStart <= intervals[i].start < prevEnd:
                # search for the right bucket to place the new meeting
                # if can be put in existing bucket, put it
                # else, create a new bucket and increment day
                if not self.findbucket(intervals[i],buckets):
                    day += 1
                    buckets.append([intervals[i]])
            else:
                prevStart, prevEnd = intervals[i].start, intervals[i].end
        
        # for bucket in buckets:
        #     for item in bucket:
        #         print(item.start,item.end)
        return day


