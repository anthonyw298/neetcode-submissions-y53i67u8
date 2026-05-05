class Solution:
    def canJump(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return True
            num = nums[i]
            count = max(count - 1, num) 
            print(count)
            if count <= 0:
                return False

















































        '''res=0
        for i in range(len(nums)):
            num=nums[i]
            if i==len(nums)-1:
                return True
            res=max(res-1,num)
            if num==0 and res==0:
                return False
        return True'''


        