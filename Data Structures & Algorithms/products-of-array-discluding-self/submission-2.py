class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res1 = [1]
        res2 = [1]
        res = []
        for i in range(len(nums) - 1):
            res1.append(res1[i] * nums[i])
        for i in range(len(nums) - 1, 0, -1):
            res2.append(res2[len(nums) - 1 - i] * nums[i])
        for i in range(len(res1)):
            res.append(res1[i] * res2[len(nums) - 1 - i])
        return res

        














































        '''#Attempt 2
        prefix=[]
        suffix=[]
        res=[]
        for i in range(len(nums)):
            if len(prefix)==0:
                prefix+=[1]
            else:
                prefix+=[prefix[i-1]*nums[i-1]]
            print(prefix)
        for i in range(len(nums)-1,-1,-1):
            print(i)
            if len(suffix)==0:
                suffix+=[1]
            else:
                suffix+=[suffix[len(nums)-i-2]*nums[i+1]]
        for i in range(len(prefix)):
            res+=[prefix[i]*suffix[len(nums)-i-1]]
        return res'''


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''prefix=[]
        suffix=[]
        res=[]
        for i in range(len(nums)):
            if i==0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1]*nums[i-1])
        for i in range(len(nums)-1,-1,-1):
            print(i)
            if i==len(nums)-1:
                print(i,'i')
                suffix.append(1)
            else:
                suffix.append(suffix[len(nums)-i-2]*nums[i+1])
        for i in range(len(nums)):
            res+=[prefix[i]*suffix[len(nums)-i-1]]
        print(prefix,suffix)
        return res'''

                