class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start > prevEnd:
                res.append([prevStart,prevEnd])
                prevStart = start
                prevEnd = end
            else:
                prevStart = min(prevStart, start)
                prevEnd = max(prevEnd, end)
        res.append([prevStart,prevEnd])
        return res






































        '''res=[]
        intervals.sort()
        prevS = intervals[0][0]
        prevL = intervals[0][1]
        for i in range(1,len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start > prevL:
                res.append([prevS,prevL])
                prevS , prevL = start, end
            else:
                prevS, prevL = min(prevS,start), max(prevL, end)
        res.append([prevS, prevL])
        return res'''



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''intervals.sort()
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
        return res'''

            
        
        