from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1 = Counter(s1)
        seen2 = {}
        l = 0
        for r in range(len(s2)):
            seen2[s2[r]] = seen2.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                seen2[s2[l]] -= 1
                if seen2[s2[l]] == 0:
                    del seen2[s2[l]]
                l += 1
            if seen1 == seen2:
                return True
            print(seen1,'seen1', seen2)
            
        return False