class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highest = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] <= 0:
                l = r
            else:
                highest = max(highest, prices[r] - prices[l])
        return highest