class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            print(stack)
            if char in "+-*/":
                print(char)
                num2 = stack.pop()
                num1 = stack.pop()
                if char == '+':
                    res = num1 + num2
                elif char == '-':
                    res = num1 - num2
                elif char == '*':
                    res = num1 * num2
                elif char =='/':
                    res = int(num1 / num2)
                stack.append(res)
            else:
                stack.append(int(char))
        return stack[-1]













































        '''stack = []
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
        return stack[-1]'''
            