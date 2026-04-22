class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(nums[l],nums[r],nums[mid])
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[l]: #left
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
            else: #right
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid  + 1
        return -1
            






































        '''#Attempt 3 
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            print(l,mid,r)
            if nums[mid]==target:
                return mid
            elif nums[mid]>=nums[l]:#left dominant
                print('left')
                if target>nums[mid] or target<nums[l]:
                    l=mid+1
                else:
                    r=mid-1
            else:#right dominant
                print('right')
                if target<nums[mid] or target>nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return -1'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''l,r = 0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            print(m,nums[l],nums[r])
            if target==nums[m]:
                return m
            if nums[l]<=nums[m]:#left sorted array
                print('hi')
                if target<nums[l] or target>=nums[m]:
                    print(nums[l],nums[r])
                    l=m+1
                else:
                    r=m-1      
            else:#right sorted array
                if target>nums[r] or target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
        return -1'''

        
        
        
        
        
        
        
        
        
        
        #attempt 1
        '''l,r=0,len(nums)-1
        m=(l+r)//2
        while nums[m]!=target and m!=l:
            if nums[l]<nums[m]:
                l=m
            elif nums[r]>nums[m]:
                r=m
            m=(l+r)//2
            print(l,m,r)
        if nums[m] == target:
            return m
        elif l==m:
            if nums[r] == target:
                return r
        return -1  '''


