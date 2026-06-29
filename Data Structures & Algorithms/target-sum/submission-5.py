class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, total):
            if total == target and i == len(nums):
                return 1
            elif i >= len(nums):
                return 0
            elif (i, total) in dp:
                return dp[(i,total)]
            add = dfs(i + 1, total + nums[i])
            sub = dfs(i + 1, total - nums[i])
            dp[(i, total)] = add + sub
            return dp[(i, total)]
        return dfs(0, 0)