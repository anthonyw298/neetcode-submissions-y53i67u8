"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        s = e = 0
        while s < len(start):
            if start[s] < end[e]:
                s += 1
                res = max(res, s - e)
            else:
                e += 1
        return res