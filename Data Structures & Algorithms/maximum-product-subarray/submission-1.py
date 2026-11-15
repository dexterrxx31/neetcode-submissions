class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = min_dp[0] = result = nums[0]

        for i in range(1, n):
            x = nums[i]

            max_dp[i] = max(x, x * max_dp[i - 1], x * min_dp[i - 1])
            min_dp[i] = min(x, x * max_dp[i - 1], x * min_dp[i - 1])

            result = max(result, max_dp[i])

        return result
