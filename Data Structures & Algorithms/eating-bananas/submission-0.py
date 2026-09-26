class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while right > left:
            mid = (left + right) // 2
            if self.hours_required(piles, mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

    def hours_required(self, piles: list[int], k: int) -> int:
        ans = 0
        for pile in piles:
            ans += math.ceil(pile / k)
        return ans
