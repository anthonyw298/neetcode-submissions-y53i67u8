class Solution:
    def hammingWeight(self, n: int) -> int:
        res=0
        while n:
            n&=n-1
            res+=1
        return res
        '''res=0
        prev=False 
        while int(n)>0:
            n=n>>1
            if prev:
                if prev>int(n):
                    res+=1
            prev=int(n)
        return res'''
        