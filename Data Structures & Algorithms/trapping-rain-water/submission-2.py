class Solution:
    def trap(self, height: List[int]) -> int:
        most = 0
        leftMax, rightMax = 0 , 0
        l, r = 0 , len(height) - 1
        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                most += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                most += rightMax - height[r]
                r -= 1
        return most
            















































        '''l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res'''
        