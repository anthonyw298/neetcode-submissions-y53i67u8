class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Attempt 2
        res=[]
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
                    if [nums[i],nums[l],nums[r]] not in res:
                        res+=[[nums[i],nums[l],nums[r]]]
                    if l<r: 
                        l+=1
                        r-=1
                    else:
                        break
                    
        return res














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