class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        high = 0
        for i in range(len(nums)):
            local = 0
            if nums[i] - 1 not in nums:
                seen.add(nums[i])
                while nums[i] + local in nums:
                    local += 1
                high = max(high, local)
        return high















































        '''#Attempt 3
        print(nums)
        print(set(nums))
        res=0
        cnt=0
        for idx,num in enumerate(nums):
            if idx!=0:
                if num-nums[idx-1]==0:
                    continue
                elif num-nums[idx-1]==1:
                    print('count incremented')
                    cnt+=1
                else:
                    print('checked')
                    if cnt>res:
                        res=cnt
                    cnt=1
            else:
                cnt+=1
        if cnt>res:
            res=cnt
        return res'''
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''if len(nums)<2:
            return len(nums)
        cnt=1
        res=0
        nums=list(sorted(set(sorted(nums))))
        print(nums,'nums')
        for i in range(1,len(nums),1):
            if nums[i]-nums[i-1]==1:
                cnt+=1
            else:
                if res<cnt:
                    res=cnt
                cnt=1
        if res<cnt:
            res=cnt
        return res'''