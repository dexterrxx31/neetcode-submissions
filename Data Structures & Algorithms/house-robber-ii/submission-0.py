class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def solve_range(start, end):
            memo = {}

            def solve(i):
                if i >= end:
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(nums[i] + solve(i + 2), solve(i + 1))
                return memo[i]

            return solve(start)

        return max(solve_range(0, n - 1), solve_range(1, n))
