class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def solve(i, prev):
            if i == len(nums):
                return 0

            if (i, prev) in memo:
                return memo[(i, prev)]

            take = 0
            if prev == -1 or nums[i] > nums[prev]:
                take = 1 + solve(i + 1, i)

            skip = solve(i + 1, prev)

            memo[(i, prev)] = max(skip, take)

            return memo[(i, prev)]

        return solve(0, -1)
