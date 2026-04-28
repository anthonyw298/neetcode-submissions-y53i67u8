class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2":'abc',
        "3":'def',
        "4":'ghi',
        "5":'jkl',
        "6":'mno',
        "7":'pqrs',
        "8":'tuv',
        "9":'wxyz',
        }
        res = []

        def dfs(i, path):
            if i >= len(digits):
                res.append("".join(path.copy()))
                return
            for c in dic[digits[i]]:
                path.append(c)
                dfs(i+1,path)
                path.pop()
            return
        dfs(0,[])
        return res if res != [""] else []


        

