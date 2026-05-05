class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        final = [0,0,0]
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            final = [max(final[0],x),max(final[1],y),max(final[2],z)]
        return final == target














































        '''res = [0,0,0]
        for a, b, c in triplets:
            if a > target[0] or b > target[1] or c > target[2]:
                continue
            else:
                res = [max(a,res[0]),max(b,(res[1])),max(c,res[2])]
        return res == target'''


