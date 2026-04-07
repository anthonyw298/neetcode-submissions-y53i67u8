class Solution:

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #Attempt 2
        cache = {}
        def dfs(i,bit):
            if i >= len(nums) - bit:
                return 0
            if (bit, i) in cache:
                return cache[(bit, i)]
            cache[(bit, i)] = max(nums[i] + dfs(i + 2, bit), dfs(i + 1, bit) )
            return cache[(bit, i)]
        return max(dfs(0,1), dfs(1,0))

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt
        '''rob1,rob2,rob3=0,0,0
        for i in range(len(nums)):
            num=nums[i]
            temp=rob1
            rob1=rob2
            rob2=rob3
            rob3=max(temp+num,rob3)
        return rob3'''