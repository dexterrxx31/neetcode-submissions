class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque(course for course in range(numCourses) if indegree[course] == 0)
        result = []

        while queue:
            course = queue.popleft()
            result.append(course)

            for neighbour in graph[course]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        if len(result) != numCourses:
            return []

        return result
