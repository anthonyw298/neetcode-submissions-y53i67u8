class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res= []
        def dfs(i, path, visit):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not visit[i]:
                    path.append(nums[i])
                    visit[i] = True
                    dfs(i,path,visit)
                    path.pop()
                    visit[i] = False

            return


        dfs(0, [], [False] * len(nums))
        return res












































        
        '''res = []

        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path, used)
                    path.pop()
                    used[i] = False

        dfs([], [False] * len(nums))
        return res'''