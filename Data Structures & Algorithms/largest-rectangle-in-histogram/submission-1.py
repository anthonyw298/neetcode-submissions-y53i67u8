class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][0]:
                stack.append([heights[i],i])
            else:
                while stack and heights[i] < stack[-1][0]:
                    height, idx = stack.pop()
                    maxArea = max(maxArea, height * (i - idx))
                stack.append([heights[i],idx])
        while stack:
                height, idx = stack.pop()
                maxArea = max(maxArea, height * ((len(heights) - idx)))
        return maxArea



