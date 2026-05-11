class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
        for i in range(len(nums)):
            prev1, prev2 = prev2, max(prev2, prev1 + nums[i])

        return prev2






















        '''
        def dfs(i, cost):
            if i >= len(nums):
                return cost
            cost = max(dfs(i + 1, cost), dfs(i + 2, cost + nums[i]))
            return cost
            

        return dfs(0, 0)'''









































        '''prev1, prev2 = 0, 0
        for i in range(2,len(nums) + 2):
            tmp = prev1
            prev1 = max(prev1, prev2 + nums[i-2])
            prev2 = tmp
        return prev1'''














































        '''#Attempt 3
        cache = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
            return cache[i]
        
        return dfs(0)'''







































        '''#Attempt 2
        rob1,rob2 = 0,0
        for num in nums:
            temp = rob1
            rob1=rob2
            rob2=max(temp+num,rob2)
        return rob2'''
        #Attempt 1
        '''sum1=sum2=0
        for i in range(len(nums)):
            if i%2==0:
                sum1+=nums[i]
            else:
                sum2+=nums[i]

        print(sum1,sum2)
        return max(sum1,sum2)'''