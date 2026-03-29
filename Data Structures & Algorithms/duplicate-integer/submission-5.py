class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup={}
        for i in nums:
            if i in dup:
                print('hi')
                return True
            else:
                print(dup)
                dup[i]=1
        return False