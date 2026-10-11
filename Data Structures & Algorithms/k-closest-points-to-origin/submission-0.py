class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        dist_heap = [(math.sqrt(x * x + y * y), [x, y]) for x, y in points]
        heapq.heapify(dist_heap)

        for i in range(k):
            ans.append(heapq.heappop(dist_heap)[1])
        return ans
