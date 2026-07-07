class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 4, 5, 6], target = 7, seen = {3:0, 4:1, 5:2, 6:3}
        # loop 1:
        # seen = {}
        # index = 0, currNum = 3, complement = 4
        # seen = {3:0}
        # loop 2: 
        # seen = {3:0}
        # index = 1, currNum = 4, complement = 3
        # return
        seen = dict()
        for index, currNum in enumerate(nums):
            complement = target - currNum
            if complement not in seen:
                seen[currNum] = index
            elif complement in seen:
                return [seen[complement], index]
            
            







































        '''
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target - nums[i]], i]
            else:
                dic[nums[i]] = i'''





































        '''
        # {} key - value we visited value: index
        visit = {}
        for i in range(len(nums)):
            if target - nums[i] in visit:
                return [visit[target - nums[i]], i]
            else:
                visit[nums[i]] = i
        '''






































        '''dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:
                return [dic[complement],i]
            dic[num] = i'''






































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

    