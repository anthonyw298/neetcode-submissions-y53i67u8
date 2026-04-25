class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i,path):
            if i >= len(nums):
                return
            if sum(path) >= target:
                if sum(path) == target:
                    res.append(path.copy())
                return
            path.append(nums[i])
            dfs(i,path)
            path.pop()
            dfs(i + 1, path)
            return
        res = []
        dfs(0,[])
        return res
            
                














































        '''#Attempt 3
        res=[]
        def dfs(i,count,subset):
            #base case
            if count>target or i>len(nums)-1:
                return 
            if count == target:
                res.append(subset[:])
                return
            #ad  
            subset.append(nums[i])
            #recurse
            dfs(i,count+nums[i],subset)
            subset.pop()
            #remove
            dfs(i+1,count,subset)
            return 
        dfs(0,0,[])
        return res'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''res=[]
        def dfs(i,curr,cnt):
            print(i,cnt)
            if i>=len(nums):
                return
            if cnt>target:
                return 
            if cnt==target:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i,curr,cnt+nums[i])
            curr.pop()
            dfs(i+1,curr,cnt)

        dfs(0,[],0)
        return res'''
        
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
