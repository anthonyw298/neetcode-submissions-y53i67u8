class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:
                return [dic[complement],i]
            dic[num] = i






































        '''
        #Attempt 2

        l , r = 0,len(nums)-1
        while l < r:
            if nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                return [l,r]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        idx=[]
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                idx+=[i]
            else:
                if len(idx)>0:
                    if nums[i]==target-nums[idx[0]]:
                        idx+=[i]
                        return idx'''

    