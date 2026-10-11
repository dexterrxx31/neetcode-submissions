class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.max_heap = [-x for x in stones]

        heapq.heapify(self.max_heap)

        while len(self.max_heap) > 1:
            x = heapq.heappop(self.max_heap)
            y = heapq.heappop(self.max_heap)

            if x < y:
                heapq.heappush(self.max_heap, x - y)

        if len(self.max_heap) == 0:
            return 0
        else:
            return -heapq.heappop(self.max_heap)
