class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Final Answer - longest strictly increasing subsequence
        #Need to know at Each Step - the length of it currenct sis
        #Recurrence Relation - cumaltive sis
        dp = [1] * (len(nums) + 1)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)
        return max(dp)






































        '''cache={len(nums):0}
        def dfs(i):
            res=1
            if i in cache:
                return cache[i]
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    res = max(res,dfs(j)+1)
            cache[i]=res
            return res

                

        for i in range(len(nums)):
            dfs(i)
        return max(cache.values())'''

        