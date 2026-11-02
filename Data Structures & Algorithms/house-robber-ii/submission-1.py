class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def solve(houses):
            dp = [0]* (len(houses)+1)

            dp[1] = houses[0]
            
            for i in range(2, len(houses) + 1):
                dp[i] = max(dp[i-1], houses[i-1] + dp[i-2])

            return dp[-1]
        
        return max(solve(nums[1:]), solve(nums[:-1]))
                

            