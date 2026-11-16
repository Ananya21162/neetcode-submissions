"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        i , n = 1, len(intervals)
        intervals.sort(key = lambda x: x.start)
        while i < n:
            o_start, o_end = intervals[i-1].start, intervals[i-1].end
            if o_start <= intervals[i].start < o_end:
                return False
            i += 1
        return True