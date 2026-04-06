class Solution:
    def countBits(self, n: int) -> List[int]:
        #4//2=2r0//2=1r0//2=0r1->100
        #nested while loop 1) for each n from 0 to n 2) to convert to bianry and count 1s
        '''res=[]
        for num in range(n+1):
            one=0
            for i in range(32):
                if num & (1<<i):
                    one+=1
            res.append(one)
        return res'''
        res = [0] * (n+1)
        offset=1
        
        for num in range(1,n+1):
            if offset*2==num:
                offset=num
            res[num]=(res[num-offset]+1)
        return res


