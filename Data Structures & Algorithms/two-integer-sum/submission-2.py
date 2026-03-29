class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            for key,value in dic.items():
                if nums[i]+key==target:
                    return [value,i]
            dic[nums[i]]=i
