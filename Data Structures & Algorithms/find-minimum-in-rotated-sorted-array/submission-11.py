class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0 , len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:
                r = mid 
            elif nums[mid] > nums[r]:
                l = mid + 1
            print(l,r)
            # (piv left) mid < right and mid > left: r = mid - 1
            # (pivleft) mid < right and mid < left: r = mid - 1
            # (piv right) mid > right and mid > left: l = mid + 1
            # (piv right) mid > right and mid < left: l = mid + 1
        return nums[l]
        





































        '''#Attempt 2
        l,r=0,len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[r]>nums[mid]:
                r=mid
            else:
                l=mid+1
        return nums[l]'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt1 
        '''if len(nums)==1 :
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
                nums=nums[:m+1]'''
