class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha=[]
        for i in range(len(s)):
            if s[i].isalpha()==True or s[i].isdigit()==True:
                alpha+=[s[i].lower()]
        alpha="".join(alpha)
        print(alpha)
        for i in range(len(alpha)):
            if alpha[i]!=alpha[len(alpha)-i-1]:
                return False
        return True