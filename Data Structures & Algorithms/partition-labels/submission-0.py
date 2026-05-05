class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c : i for i, c in enumerate(s)}
        res, size, end = [], 1, 0
        for i in range(len(s)):
            end = max(end,last[s[i]])
            if i == end:
                res.append(size)
                size = 1
            else:
                size += 1
        return res
                


