class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openCount,closeCount,path):
            if len(path) == 2 * n:
                res.append("".join(path.copy()))
                return
            elif openCount < closeCount:
                return
            if openCount < n:
                path.append('(')
                dfs(openCount + 1, closeCount, path)
                path.pop()
            if closeCount < n:
                path.append(')')
                dfs(openCount, closeCount + 1, path)
                path.pop()
            return
            
        dfs(0,0,[])
        return res