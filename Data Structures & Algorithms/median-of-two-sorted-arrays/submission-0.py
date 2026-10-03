class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        l = n + m
        i, j = 0, 0
        curr, prev = 0, 0
        count = 0
        while count <= l / 2:
            prev = curr
            if i < n and j < m:
                if nums1[i] <= nums2[j]:
                    curr = nums1[i]
                    i += 1
                else:
                    curr = nums2[j]
                    j += 1
            elif i < n:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1
            count += 1
        if l % 2 == 1:
            return curr
        else:
            return (prev + curr) / 2
