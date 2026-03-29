class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.replace(' ','')
        s=s.lower()
        bruh=''
        for i in range(len(s)):
            if s[i].isalpha() ==True or s[i].isdigit()==True:
                bruh+=s[i]
        s=bruh
        print(s)
        if len(s)==1:
            return True
        for i in range(len(s)//2):
            print(s[i],s[len(s)-i-1])
            if s[i]!=s[len(s)-i-1]:
                return False
        return True
