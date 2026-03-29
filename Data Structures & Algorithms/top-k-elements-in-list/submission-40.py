class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        lst=[]
        for i in nums:
            if i in dic:
                dic[i]+=1 
            else:
                dic[i]=1
        while k>0:
            print(dic,max(dic))
            lst+=[max(dic, key=dic.get)]
            dic.pop(max(dic, key=dic.get))
            k-=1
        return lst
