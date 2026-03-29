class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return nums[0]
        return max(self.helper(nums[1:]),
                            self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for num in nums:
            temp=rob1
            rob1=rob2
            rob2=max(temp+num,rob2)
        return rob2