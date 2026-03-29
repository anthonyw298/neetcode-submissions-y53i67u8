class Solution:
    def maxArea(self, heights: List[int]) -> int:
        end=len(heights)-1
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

        return maxx

