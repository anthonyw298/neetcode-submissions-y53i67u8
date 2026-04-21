from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = Counter(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] not in seen:
                seen = Counter(s1)
                l = r + 1
                continue
            while seen[s2[r]] == 0:
                seen[s2[l]] += 1
                l += 1
            seen[s2[r]] -= 1
            if r - l + 1 == len(s1):
                return True
        return False