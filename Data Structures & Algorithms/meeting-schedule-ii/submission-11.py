"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        startTimes = [i.start for i in intervals]
        startTimes.sort()
        endTimes = [i.end for i in intervals]
        endTimes.sort()
        s, e, res, curr = 0, 0, 0, 0
        while s < len(startTimes):
            if startTimes[s] < endTimes[e]:
                s += 1
                curr += 1
            else:
                res = max(res, curr)
                curr -= 1
                e += 1
        res = max(res, curr)
        return res
