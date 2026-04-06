class Solution:
    def countBits(self, n: int) -> List[int]:
        #4//2=2r0//2=1r0//2=0r1->100
        #nested while loop 1) for each n from 0 to n 2) to convert to bianry and count 1s
        res=[]
        for num in range(n+1):
            one=0
            for i in range(32):
                if num & (1<<i):
                    one+=1
            res.append(one)
        return res

