class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        
            l, r = i , i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        return count













































        
        '''total=0
        for  i in range(len(s)):
            #even length
            l,r=i,i
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                total+=1
                l-=1
                r+=1
            print(s[l+1:r],1)
            l,r=i,i+1
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                total+=1
                l-=1
                r+=1
            print(s[l+1:r],2)

        return total'''

        