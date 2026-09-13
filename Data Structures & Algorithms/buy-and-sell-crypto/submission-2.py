class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices)
        l_min = 101
        profit = 0
        while l < r:
            l_min = min(l_min, prices[l])
            profit = max(profit, prices[l] - l_min)
            l += 1
        return profit
