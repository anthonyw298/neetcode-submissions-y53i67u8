class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.robber(0,nums[:-1]), self.robber(1,nums))
    def robber(self, i, nums):
        prev1, prev2 = 0, 0
        while i < len(nums):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[i])
            prev2 = temp
            i += 1
        return prev1
        
        