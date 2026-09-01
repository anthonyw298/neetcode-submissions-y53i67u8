class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        l = 0
        final = 0
        for r in range(len(s)):
            while s[r] in curr:
                final = max(len(curr), final)
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
        final = max(len(curr), final)    
        return final