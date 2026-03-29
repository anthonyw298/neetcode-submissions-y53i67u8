class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Attempt 2
        nodupe=set(nums)
        if len(nodupe)<len(nums):
            return True
        return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    



        
        #Attempt 1
        '''dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            else:
                dic[nums[i]]=1
        return False'''