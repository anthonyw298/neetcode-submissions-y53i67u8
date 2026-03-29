class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1 :
            return nums[0]
        l,r=0,len(nums)-1
        while len(nums)>1:
            l,r=0,len(nums)-1
            m=(len(nums)-1)//2
            print(l,m,r,nums)
            if len(nums)==1:
                return nums[0]
            elif len(nums)==2:
                return min(nums[0],nums[1])
            elif len(nums)==3:
                return min(nums[0],nums[1],nums[2])
            if nums[m]>nums[l] and nums[m]<nums[r]:
                nums=nums[:m+1]
            elif nums[m]>nums[l] and nums[m]>nums[r]:
                nums=nums[m+1:]
            elif nums[m]<nums[l] and nums[m]>nums[r]:
                nums=nums[:m+1]
            else:
                nums=nums[:m+1]
                #nums[m]>nums[l] nums[m]>nums[r] larger
                #nums[m]<nums[l] nums[m]<nums[r] smaller
                #nums=nums[m:] right
                #nums=nums[:m] left
            print(nums)