class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        s = s.lower()
        l , r = 0, len(s) - 1
        while l <= r:
            while r > l and not s[r].isalnum():
                r -= 1
            while l < r and not s[l].isalnum():
                l += 1
            if s[r] != s[l]:
                print(s[r],s[l])
                return False
            r -= 1
            l += 1
        return True














































        '''#Attempt 3
        l, r = 0, len(s)-1
        while l<r:
            while s[l].isalnum()==False and l<len(s)-1:
                l+=1
                print(l)
            while s[r].isalnum()==False and r>0:
                r-=1
            if l>=r:
                return True
            if s[l].lower()!=s[r].lower():
                print(s[l],s[r])
                return False
            else:
                print('hi')
                l+=1
                r-=1
        return True'''
            
            



















        
        
        
        
        
        
        #Attempt 2
        '''l,r = 0,len(s)-1
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
        return True'''