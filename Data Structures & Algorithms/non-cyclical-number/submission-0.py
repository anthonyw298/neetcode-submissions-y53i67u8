class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        def square(n):
            res=0
            while n>0:
                res+=(n%10)**2
                n//=10
            return res
        while n!=1:
            n=square(n)
            if n in seen:
                return False
            seen.add(n)
        return True