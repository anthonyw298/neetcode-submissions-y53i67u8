class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,res = 0, 0, 0
        dic={}
        while r<len(s):
            print(l,r)
            if s[r] in dic:
                print('hit')
                if res<max(len(dic),r-l):
                    res=max(len(dic),r-l)
                print(res,'res')
                while s[r] in dic:
                    l+=1
                    dic.pop(next(iter(dic)))
            dic[s[r]]=1
            r+=1
            print(dic)
        if res<max(len(dic),r-l):
            res=max(len(dic),r-l)
        print(l,r)
        return res

        