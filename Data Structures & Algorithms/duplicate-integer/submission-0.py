class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newlst={}
        for x in nums:
            if x in newlst:
                return True
            newlst[x]=1
            print(newlst)
        return False