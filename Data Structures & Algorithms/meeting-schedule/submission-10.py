"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = []
        intervals.sort(key = lambda i:i.start)
        if not intervals:
            return True
        prevEnd = intervals[0].end
        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if prevEnd > start:
                return False
            prevEnd = end
        return True


































        '''if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        prev=intervals[0].end
        for i in range(1,len(intervals)):
            start=intervals[i].start
            end=intervals[i].end
            if start<prev:
                return False
            prev=end
        return True'''
        