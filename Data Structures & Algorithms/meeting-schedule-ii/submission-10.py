"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        res=[intervals[0].end]
        for i in range(1,len(intervals)):
            p=0
            start=intervals[i].start
            end=intervals[i].end
            while p<len(res):
                if res[p]<=start:
                    break
                else:
                    p+=1
            if p==len(res):
                res.append(end)
            else:
                res[p]=end
        print(res)
        return len(res)
            

        