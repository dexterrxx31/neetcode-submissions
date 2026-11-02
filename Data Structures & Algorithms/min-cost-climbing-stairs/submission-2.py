class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n + 2)
        next1 = next2 = 0
        for i in range(n-1,-1,-1):
            curr = cost[i] + min(next1, next2)
            next1 = next2
            next2 = curr

        return min(next1, next2)