class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(houses):
            prev1 = prev2 = 0

            for money in houses:
                curr = max(prev1, money + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(solve(nums[:-1]), solve(nums[1:]))
