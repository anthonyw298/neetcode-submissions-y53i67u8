class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Attempt 2
        val=[]
        from collections import Counter
        lst=Counter(nums)
        lst = lst.most_common()
        print(lst,'base')
        while len(lst)>k:
            lst.pop()
        print(lst)
        for num in lst:
            val+=[num[0]]
        return val
        #Attempt 1
        '''if len(nums)==k:
            return nums
        dic={}
        lst=[]
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        return lst'''



        
