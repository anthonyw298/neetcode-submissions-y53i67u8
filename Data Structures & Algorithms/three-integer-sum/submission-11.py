class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l  += 1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    r -= 1
                    l += 1
        return res


















































        '''#Attempt 4
        nums.sort()
        print(nums)
        if nums[0] > 0:
            return []
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                l = i + 1
                r = len(nums) - 1
                while l < r:
                    if nums[l] + nums[r] + nums[i] > 0:
                        r -= 1
                    elif nums[l] + nums[r] + nums[i] < 0:
                        l += 1
                    else:
                        res.append([nums[l],nums[r],nums[i]])
                        while l < len(nums) - 1 and nums[l] == nums[l + 1]:
                            l += 1
                        while r > l and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res'''















































        #Attempt 3
        '''res=[]
        nums=sorted(nums)
        print(nums)
        for i in range(len(nums)-2):
            l=i+1
            r=len(nums)-1
            target=0-nums[i]
            while l<r:
                if nums[l]+nums[r]>target:
                    r-=1
                elif nums[l]+nums[r]<target:
                    l+=1
                else:
                    if [nums[l],nums[r],nums[i]] not in res:
                        res+=[[nums[l],nums[r],nums[i]]]
                    l+=1
                    r-=1
        print(res)
        return res'''

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 2
        '''res=[]
        nums.sort()
        print(nums)
        for i,num in enumerate(nums):
            if num>0:
                break
            l,r = i+1, len(nums)-1
            while l < r:
                if nums[i]+nums[l]+nums[r]<0:
                    l+=1
                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l+=1
                    r-=1
                    
        return res'''














        #Attempt 1
        '''j=-1
        k=1
        res=[]
        nums.sort()
        print(nums)
        for i in range(1,len(nums)-1,1):

            while 0-nums[i]!= nums[i+j]+nums[i+k]:
                print(i,j,k)
                if 0-nums[i]>nums[i+j]+nums[i+k]:
                    print(k,'k')
                    k+=1
                elif 0-nums[i]<nums[i+j]+nums[i+k]:
                    print('b')
                    j-=1
                print(k,'kk')
                if abs(j)>len(nums)-i-1 or k>len(nums)-i-1:
                    print('broke')
                    j=-1
                    k=1
                    break
            if 0-nums[i]==nums[i+j]+nums[i+k]:
                if [nums[i],nums[i+j],nums[i+k]] not in res:
                    res+=[[nums[i],nums[i+j],nums[i+k]]]
            j=-1
            k=1
        return res'''