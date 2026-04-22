class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def TorF(num):
            count = 0
            for char in piles:
                count += -(-char // num)
            if count <= h:
                return True
            return False
        l , r = 1 , max(piles)
        while l <= r:
            mid = (l + r) // 2
            if l == r:
                return l
            elif TorF(mid):
                r = mid
            else:
                l = mid + 1
        






































        '''#[0-9 f,f,f,f,f,t,t,t,]
        left, right = 1, max(piles)
        def valid(k):
            count = 0
            for pile in piles:
                count += (pile + k - 1) // k
            return count <= h

        while left < right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid
            else:
                left = mid + 1
        return left'''