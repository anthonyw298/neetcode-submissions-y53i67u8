class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k:
            x = min(nums)
            for i in range(len(nums)):
                if nums[i] == x:
                    nums[i] *= multiplier
                    break
            k -= 1
        return nums