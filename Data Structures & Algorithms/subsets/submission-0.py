class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, path = [], []

        def bt(index):
            # base case
            if index == len(nums):
                result.append(path.copy())
                return

            # choose
            path.append(nums[index])
            bt(index + 1)
            # skip
            path.pop()
            bt(index + 1)

        bt(0)
        return result
