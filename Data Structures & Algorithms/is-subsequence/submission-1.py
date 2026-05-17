class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pS = 0
        for pT in range(len(t)):
            if pS == len(s):
                return True
            if t[pT] == s[pS]:
                pS += 1
        return pS == (len(s))