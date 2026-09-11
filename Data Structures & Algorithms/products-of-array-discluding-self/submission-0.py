class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # zero will create a edge case now
        r = [0] * len(nums)
        zero_count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index = i
                zero_count += 1
                if zero_count > 1:
                    return r

        if zero_count == 1:
            pr = 1
            for n in nums:
                if n == 0:
                    continue
                pr *= n
            r[zero_index] = pr
            return r

        tpr = 1
        for n in nums:
            tpr *= n

        for i in range(len(nums)):
            r[i] = tpr // nums[i]

        return r
