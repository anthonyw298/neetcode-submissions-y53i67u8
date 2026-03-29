class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        cnt=1
        res=0
        nums=list(sorted(set(sorted(nums))))
        print(nums,'nums')
        for i in range(1,len(nums),1):
            if nums[i]-nums[i-1]==1:
                cnt+=1
            else:
                if res<cnt:
                    res=cnt
                cnt=1
        if res<cnt:
            res=cnt
        return res