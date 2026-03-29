class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx=[]
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                idx+=[i]
            else:
                if len(idx)>0:
                    if nums[i]==target-nums[idx[0]]:
                        idx+=[i]
                        return idx

    