class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []

        for r, n in enumerate(nums):
            while dq and nums[dq[-1]] < n:
                dq.pop()
            dq.append(r)

            if dq[0] <= r - k:
                dq.popleft()

            if r >= k - 1:
                res.append(nums[dq[0]])

        return res
