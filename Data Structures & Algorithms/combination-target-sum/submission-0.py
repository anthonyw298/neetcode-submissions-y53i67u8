class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #Attempt 2
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
        
        #Attempt 1
        '''final=[]
        res= []
        subset=[]
        def backtrack(i):
            if i>=len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            backtrack(i+1)
            subset.pop()
            backtrack(i+1)
        backtrack(0)
        for i in res:
            if sum(i)==target:
                final+=[i]
        return final'''
