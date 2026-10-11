class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_heap = [(-freq, task) for task, freq in Counter(tasks).items()]
        heapq.heapify(task_heap)
        cool_down_queue = deque()
        time = 0
        while task_heap or cool_down_queue:
            while cool_down_queue and cool_down_queue[0][1] <= time:
                taskq = cool_down_queue.popleft()
                heapq.heappush(task_heap, (taskq[0], taskq[2]))

            if not task_heap and cool_down_queue:
                time = cool_down_queue[0][1]
                continue

            freq, task = heapq.heappop(task_heap)

            if freq + 1:
                cool_down_queue.append((freq + 1, time + n + 1, task))

            time += 1

        return time
