class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            try:
                stack.append(int(char))
            except ValueError:
                char2 = stack.pop()
                char1 = stack.pop()
                if char == '+':
                    final = char1 + char2
                elif char == '-':
                    final = char1 - char2
                elif char == '*':
                    final = char1 * char2
                elif char == '/':
                    final = int(char1 / char2)
                stack.append(final)
        return stack[-1]
            