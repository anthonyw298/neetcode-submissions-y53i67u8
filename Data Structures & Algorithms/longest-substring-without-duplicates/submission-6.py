class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        most = 0
        for r in range(len(s)):
            while s[r] in seen:
                most = max(most,len(seen))
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
        most = max(most,len(seen))
        return most














































        '''#Attempt 2
        l,dic,res=0,{},0
        if len(s) == 1:
            return 1
        for r in range(len(s)):
            while s[r] in dic:
                res=max(res,len(dic))
                dic.pop(s[l])
                l+=1
            dic[s[r]]=1
        res=max(res,len(dic))
        return res'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Attempt 1
        '''l,r,res = 0, 0, 0
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
        return res'''

        