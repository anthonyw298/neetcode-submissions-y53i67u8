class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''dic_1={}
        dic_2={}
        for i in range(len(s)):
            if s[i] in dic_1:
                dic_1[s[i]]+=1
            else:
                dic_1[s[i]]=1
        for i in range(len(t)):
            if t[i] in dic_2:
                dic_2[t[i]]+=1
            else:
                dic_2[t[i]]=1
        if dic_1==dic_2:
            return True
        else:
            return False'''
        if len(s)!=len(t):
            return False
        count= [0]*26
        for i in s:
            count[ord(i)-ord('a')]+=1
        for i in t:
            count[ord(i)-ord('a')]-=1
            if count[ord(i)-ord('a')]<0:
                return False
        return True

