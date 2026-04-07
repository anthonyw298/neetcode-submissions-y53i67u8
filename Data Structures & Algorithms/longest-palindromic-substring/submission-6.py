class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = ""
        for i in range(len(s)):
            l, r = i , i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
            l , r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(s[l:r+1]) > resLen:
                    res = s[l:r+1]
                    resLen = len(res)
                l -= 1
                r += 1
        return res









































        '''res=""
        for i in range(len(s)):
            #odd length
                l,r=i,i
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    l-=1
                    r+=1
                if len(s[l+1:r]) > len(res):
                    res=s[l+1:r]
                l,r=i,i+1
                while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                    l-=1
                    r+=1
                if len(s[l+1:r]) > len(res):
                    res=s[l+1:r]
        return res'''

