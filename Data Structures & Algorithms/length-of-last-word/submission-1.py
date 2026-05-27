class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = (len(s) - 1)
        total = 0
        while True:
            if i < 0:
                return total
            elif s[i] == " " and not total:
                i -= 1
            elif s[i] == " " and total:
                return total
            else:
                total += 1
                i -= 1