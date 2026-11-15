class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = min_prod = result = nums[0]

        for x in nums[1:]:
            a = x
            b = x * max_prod
            c = x * min_prod

            max_prod = max(a, b, c)
            min_prod = min(a, b, c)

            result = max(result, max_prod)
        return result
