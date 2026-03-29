class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s={}
        dic_t={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] in dic_s:
                dic_s[s[i]]+=1
            else:
                dic_s[s[i]]=1
            if t[i] in dic_t:
                dic_t[t[i]]+=1
            else:
                dic_t[t[i]]=1
        if dic_t != dic_s:
            return False
        return True

