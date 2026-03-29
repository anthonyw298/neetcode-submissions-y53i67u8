class Solution:
    def countSubstrings(self, s: str) -> int:
        total=0
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

        return total

        