class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def solve(i):
            if i >= n:
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(solve(i + 1), nums[i] + solve(i + 2))

            return memo[i]

        return solve(0)
