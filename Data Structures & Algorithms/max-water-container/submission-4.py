class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Attempt 2
        l,r,res = 0,len(heights)-1,0
        while l<r:
            res=max(res,min(heights[l],heights[r])*(r-l))
            print(res)
            if heights[r]>heights[l]:
                l+=1
            else:
                r-=1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''end=len(heights)-1
        begin=0
        maxx=0
        while begin<end:
            print(begin,end)
            if min(heights[begin],heights[end])*(end-begin) > maxx:
                maxx=min(heights[begin],heights[end])*(end-begin)
            
            if heights[begin]>=heights[end]:
                end-=1
            else:
                begin+=1

        return maxx'''

