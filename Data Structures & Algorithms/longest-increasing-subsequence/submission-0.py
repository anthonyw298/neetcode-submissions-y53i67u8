class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache={len(nums):0}
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
        return max(cache.values())

        