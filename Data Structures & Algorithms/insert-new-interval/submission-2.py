class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval[0] , newInterval[1]
        res = []
        for start,end in intervals:
            if end < newStart:
                res.append([start,end])
            elif start > newEnd:
                res.append([newStart, newEnd])
                res.append([start,end])
                newStart = newEnd = float('inf')
            else:
                newStart, newEnd = min(newStart,start), max(newEnd, end)
        if newStart != float('inf'):
            res.append([newStart,newEnd])
        return res














































    '''#Attempt 2
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
        return res'''
            
        #Attempt 1
    '''res=[]
        newStart=newInterval[0]
        newEnd=newInterval[1]
        for start,end in intervals:
            if newStart>end or newEnd < start:
                res.append([start,end])
            else:'''
                
                


        