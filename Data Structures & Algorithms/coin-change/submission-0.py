class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def solve(amount):
            if amount == 0:
                return 0

            if amount < 0:
                return float("inf")

            if amount in memo:
                return memo[amount]

            minimum = float("inf")

            for coin in coins:
                result = 1 + solve(amount - coin)
                minimum = min(minimum, result)

            memo[amount] = minimum

            return minimum

        answer = solve(amount)
        return answer if answer != float("inf") else -1
