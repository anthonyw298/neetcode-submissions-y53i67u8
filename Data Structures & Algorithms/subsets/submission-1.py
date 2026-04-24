class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i, path):
            if i >= len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)
            return 
            
    
        res = []
        dfs(0,[])
        return res
                  
















































        '''res = []
        def dfs(i,path):
            if i == len(nums):
                res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i+1,path)
            path.pop()
            dfs(i+1,path)
            return
        dfs(0, [])
        return res'''