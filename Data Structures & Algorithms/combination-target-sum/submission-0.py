class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, path = [], []

        def bt(start, remaining):
            if remaining == 0:
                result.append(path.copy())
                return

            for i in range(start, len(nums)):
                num = nums[i]

                if num > remaining:
                    continue

                path.append(num)
                bt(i, remaining - num)
                path.pop()

        bt(0, target)
        return result
