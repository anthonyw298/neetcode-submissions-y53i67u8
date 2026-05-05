class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local, glob = 0, nums[0]
        for num in nums:
            local += num
            glob = max(local, glob)
            if local < 0:
                local = 0
        return glob














































        '''local=0
        glob=nums[0]
        for num in nums:
            local=max(num,local+num)
            glob=max(glob,local)
        return glob'''
        