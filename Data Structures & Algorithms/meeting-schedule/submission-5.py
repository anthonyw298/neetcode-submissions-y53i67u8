"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        lst=[]
        for i in range(len(intervals)):
            for j in range(intervals[i].start,intervals[i].end,1):
                if j not in lst:
                    lst+=[j]
                else:
                    return False
        return True
        

