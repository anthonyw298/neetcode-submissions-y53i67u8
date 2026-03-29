class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Attempt #3
        freq={}
        res=[]
        bucket=[[] for i in range(len(nums)+1)]
        for num in nums:
            freq[num]=1+freq.get(num,0)
        for key,value in freq.items():
            bucket[value]+=[key]
        for i in range(len(bucket)-1,0,-1):
            for j in bucket[i]:
                if len(res)<k:
                    print(j)
                    res+=[j]
        return res
        #Attempt 2
        '''val=[]
        from collections import Counter
        lst=Counter(nums)
        lst = lst.most_common()
        print(lst,'base')
        while len(lst)>k:
            lst.pop()
        print(lst)
        for num in lst:
            val+=[num[0]]
        return val'''
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



        
