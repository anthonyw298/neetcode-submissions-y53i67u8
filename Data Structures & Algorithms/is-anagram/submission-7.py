from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = Counter(s)
        for char in t:
            if char not in word or word[char] == 0:
                return False
            word[char] -=1
        return sum(word.values()) == 0





































        '''#Attempt 2
        dic_s={}
        dic_t={}
        for char in s:
            dic_s[char]=1+dic_s.get(char,0)
        for char in t:
            dic_t[char]=1+dic_t.get(char,0)
        if dic_s!=dic_t:
            return False
        return True'''





















        
        
        
        
        #Attempt 1
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
            return False
        if len(s)!=len(t):
            return False
        count= [0]*26
        for i in s:
            count[ord(i)-ord('a')]+=1
        for i in t:
            count[ord(i)-ord('a')]-=1
            if count[ord(i)-ord('a')]<0:
                return False
        return True'''

