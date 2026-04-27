class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def dfs(i,path):
            if i >= len(s):
                res.append(path.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    path.append(s[i:j+1])
                    dfs(j+1,path)
                    path.pop()
        def isPalindrome(path):
            l, r = 0, len(path) - 1
            while l<r:
                if path[l] == path[r]:
                    l += 1
                    r -=1
                else:
                    return False
            return True
        dfs(0,[])
        return res