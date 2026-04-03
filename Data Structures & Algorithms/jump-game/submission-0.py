class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=0
        for i in range(len(nums)):
            num=nums[i]
            if i==len(nums)-1:
                return True
            res=max(res-1,num)
            print(res,num)
            if num==0 and res==0:
                return False
        return True


        