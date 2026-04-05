class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Attempt 1
        intervals.sort()
        res=[]
        newInterval=intervals[0]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if start>newInterval[1]:
                res.append(newInterval)
                newInterval=intervals[i]
            else:
                newInterval=[min(start,newInterval[0]),max(end,newInterval[1])]
        res.append(newInterval)
        return res

            
        
        