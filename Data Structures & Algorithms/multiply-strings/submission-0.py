class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int1 = []
        int2 = []
        for num in num1:
            int1.append(ord(num)-ord('0'))
        for num in num2:
            int2.append(ord(num)-ord('0'))
        int1.reverse()
        int2.reverse()
        
        res = [0] * (len(num1) + len(num2))
        for i in range(len(int1)):
            for j in range(len(int2)):
                res[i + j] += int1[i] * int2[j]
                res[i + j + 1] += res[i + j] // 10
                res[i + j] %= 10
        res.reverse()
        return "".join(str(d) for d in res).lstrip("0") or "0"


