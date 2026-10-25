class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    return False  # this is cycle

                if not dfs(neighbour, node):
                    return False

            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n
