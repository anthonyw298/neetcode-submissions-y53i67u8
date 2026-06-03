class Solution:
    def minWindow(self, s: str, t: str) -> str:
        sd = {}
        td = Counter(t)
        have = l = 0
        need = len(td) 
        res = ""
        minLen = float('inf')
        for r in range(len(s)):
            sd[s[r]] = sd.get(s[r], 0) + 1
            if s[r] in td and sd[s[r]] == td[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    res = s[l:r + 1]
                sd[s[l]] -= 1
                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -= 1
                l += 1
        return res


        