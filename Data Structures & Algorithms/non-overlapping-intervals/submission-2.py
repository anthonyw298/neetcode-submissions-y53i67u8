class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res=0
        prevEnd=intervals[0][1]
        for i in range(1,len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if start>=prevEnd:
                print('a')
                prevEnd=end
            else:
                print('b')
                prevEnd=min(end,prevEnd)
                res+=1
        return res






        