class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Attempt 2
        # 1) final answer is largest product within the array
        # 2) the largest product at the index dp[i] = dp[]?
        # 3) the product of the bigger problem will be using the product of a subproblem * that current product
        maxProd = nums[0]
        minProd = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp = minProd
            minProd = min(nums[i], minProd * nums[i], maxProd * nums[i])
            maxProd = max(nums[i], temp * nums[i], maxProd * nums[i])
            res = max(res, maxProd)
        return res

















































        #Attemopt 1
        '''res=max(nums)
        curMin,curMax=1,1
        for n in nums:
            temp=curMax
            curMax=max(n*curMax,n*curMin,n)
            curMin=min(n*temp,n*curMin,n)
            res=max(res,curMax)
        return res'''