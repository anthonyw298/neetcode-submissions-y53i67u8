class Solution:
    def rob(self, nums: List[int]) -> int:
        #Attempt 2
        rob1,rob2 = 0,0
        for num in nums:
            temp = rob1
            rob1=rob2
            rob2=max(temp+num,rob2)
        return rob2
        #Attempt 1
        '''sum1=sum2=0
        for i in range(len(nums)):
            if i%2==0:
                sum1+=nums[i]
            else:
                sum2+=nums[i]

        print(sum1,sum2)
        return max(sum1,sum2)'''