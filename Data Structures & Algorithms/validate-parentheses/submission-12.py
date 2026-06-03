class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        match = {'}':'{', ')':'(', ']':'['}
        stack = []
        for i in range(len(s)):
            if s[i] in match.values():
                stack.append(s[i])
            else:
                if not stack or stack[-1] != match[s[i]]:
                    return False 
                else:
                    stack.pop()
        return len(stack) == 0