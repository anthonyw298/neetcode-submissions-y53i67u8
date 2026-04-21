class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res= []
        q = deque([])
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if l > q[0]:
                q.popleft()
            if (r + 1) >= k:
                res.append(nums[q[0]])
                
                l += 1
            r += 1
        return res
        '''res = []
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
        return res'''

