class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        best = 0

        for n in nums:
            if n - 1 in nums:
                continue
            l = 1
            while n + l in nums:
                l += 1
            best = max(best, l)

        return best
