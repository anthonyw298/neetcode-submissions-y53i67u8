class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        l = 0
        res = 0
        count = {}
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            while sum(count.values()) - max(count.values()) > k:
                count[s[l]] = count.get(s[l], 0) - 1
                l+=1
            res = max(res,sum(count.values()))
        return res
        




















































        #Attempt 2- Brute Force? -sum
        '''l,res,dic=0,0,{}
        if k>=len(s):
            return len(s)
        for r in range(len(s)):
            dic[s[r]]=1+dic.get(s[r],0)
            while sum(dic.values())-max(dic.values())>k:
                res=max(res,sum(dic.values())-1)
                dic[s[l]]-=1
                l+=1
                print(dic,'1')
            print(dic,'2')
        print(dic,'3')
        return max(res,sum(dic.values()))'''
























        #Attempt 1
        '''l , r, res = 0,0,0
        dic={}
        if r==0:
            dic[s[r]]=1+dic.get(s[r],0)
            r+=1
        print(dic)
        while r<len(s):
            while max(dic.values())+k>=sum(dic.values()):
                dic[s[r]]=1+dic.get(s[r],0)
                r+=1
                if r==len(s):
                    break
                print(dic)
            if res<max(dic.values())+ min(sum(dic.values()) - max(dic.values()), k): 
                res=max(dic.values())+ min(sum(dic.values()) - max(dic.values()), k)
                print(res)
            while max(dic.values())+k<sum(dic.values()):
                dic[s[l]]=dic.get(s[l],0)-1
                l+=1
                print(dic)
            print(max(dic.values()))
        if res<max(dic.values())+ min(sum(dic.values()) - max(dic.values()), k): 
                res=max(dic.values())+ min(sum(dic.values()) - max(dic.values()), k)
                print(res)
        print(dic)
        return res'''


            


        