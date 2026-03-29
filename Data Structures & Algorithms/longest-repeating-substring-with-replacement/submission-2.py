class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l , r, res = 0,0,0
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
        return res


            


        