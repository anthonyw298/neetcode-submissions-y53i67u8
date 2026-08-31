class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res1, res2 = [1], [1]
        for i in range(1, len(nums)):
            res1.append(nums[i -1] * res1[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            res2.append(nums[i + 1] * res2[len(nums) - i - 2])
        res = []
        res2.reverse()

        for i in range(len(nums)):
            res.append(res1[i] * res2[i])
        return res