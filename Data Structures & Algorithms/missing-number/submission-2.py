class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        dp= [-1] * (len(nums)+1)
        for i,num in enumerate(nums):
            dp[num]=num
        print(dp)
        for i,num in enumerate(dp):
            if num==-1:
                return i



    
        