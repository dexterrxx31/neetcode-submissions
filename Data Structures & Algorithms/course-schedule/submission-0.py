class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for c, p in prerequisites:
            graph[p].append(c)

        states = [0] * numCourses

        def dfs(c):
            if states[c] == 1:
                return False
            if states[c] == 2:
                return True

            states[c] = 1

            for n in graph[c]:
                if not dfs(n):
                    return False

            states[c] = 2

            return True

        for c in range(numCourses):
            if states[c] == 0:
                if not dfs(c):
                    return False

        return True
