class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        count = 0
        for temp in temperatures:
            print(stack,res)
            while stack and temp > stack[-1][0]:
                 pair = stack.pop()
                 day = pair[1]
                 res[day] = count - day
            stack.append([temp, count])
            count += 1
        while stack:
            pair = stack.pop()
            day = pair[1]
            res[day] = 0
        return res
        