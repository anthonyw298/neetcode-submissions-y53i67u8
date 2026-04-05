class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Attempt 2
        res=[]
        for i in range(len(intervals)):
            start=intervals[i][0]
            end=intervals[i][1]
            if start>newInterval[1]:
                res.append(newInterval)
                return res+intervals[i:]
            elif end<newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval=[min(start,newInterval[0]),max(end,newInterval[1])]
        res.append(newInterval)
        return res
            
        #Attempt 1
        '''res=[]
        newStart=newInterval[0]
        newEnd=newInterval[1]
        for start,end in intervals:
            if newStart>end or newEnd < start:
                res.append([start,end])
            else:'''
                
                


        