class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local=0
        glob=nums[0]
        for num in nums:
            local=max(num,local+num)
            glob=max(glob,local)
        return glob
        