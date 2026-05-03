class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        half = total // 2
        print(half)
        dp = [False] * (half + 1)
        dp[0] = True
        for num in nums:
            for i in range(len(dp)-1,num-1,-1):
                dp[i] = dp[i - num] or dp[i]
        print(dp)
        return dp[len(dp) - 1]
        













































        '''if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        currSum = 0
        dp = [False] * (target + 1)
        dp[0] = True
        for i in range(len(nums)):
            for j in range(target,i):
                if dp[i-j]:
                    dp[i] = dp[i-j] or dp[i]
        print(dp)
        return dp[len(dp) - 1]'''
        