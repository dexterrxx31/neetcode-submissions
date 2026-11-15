class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        memo = {}

        def solve(i, remaining):
            if remaining == 0:
                return True

            if i == len(nums) or remaining < 0:
                return False

            if (i, remaining) in memo:
                return memo[(i, remaining)]

            take = solve(i + 1, remaining - nums[i])
            skip = solve(i + 1, remaining)
            memo[(i, remaining)] = take or skip
            return memo[(i, remaining)]

        return solve(0, target)
