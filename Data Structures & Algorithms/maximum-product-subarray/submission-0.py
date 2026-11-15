class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        memo = {}

        def solve(i):
            if i == 0:
                return nums[0], nums[0]

            if i in memo:
                return memo[i]

            prev_max, prev_min = solve(i - 1)

            x = nums[i]

            curr_max = max(x, x * prev_max, x * prev_min)
            curr_min = min(x, x * prev_max, x * prev_min)

            memo[i] = (curr_max, curr_min)

            return memo[i]

        result = nums[0]

        for n in range(len(nums)):
            curr_max, _ = solve(n)
            result = max(result, curr_max)

        return result
