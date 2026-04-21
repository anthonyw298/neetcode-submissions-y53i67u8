class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        seen = {}
        for r in range(len(nums)):
            seen[nums[r]] = seen.get(nums[r], 0) + 1
            if sum(seen.values()) > k:
                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1
            if sum(seen.values()) == k:
                res.append(max(seen))
        return res

