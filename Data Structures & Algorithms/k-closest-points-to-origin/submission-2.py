class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_heap = [(math.sqrt(x * x + y * y), [x, y]) for x, y in points]
        heapq.heapify(dist_heap)
        return [heapq.heappop(dist_heap)[1] for i in range(k)]
