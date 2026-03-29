class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Attempt 1
        l,r = 0,len(s)-1
        while l<r:
            while s[l].isalpha()==False and s[l].isdigit()==False and l<r:
                l+=1
            while s[r].isalpha()==False and s[r].isdigit()==False and l<r:
                r-=1
            print(s[l].islower(),s[r].lower())
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True