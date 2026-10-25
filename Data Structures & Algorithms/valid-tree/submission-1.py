class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # for trees number of edges must be equal to node - 1
        if len(edges) != n - 1:
            return False

        # Creating empty graph
        graph = [[] for _ in range(n)]

        # Creating a undirected graph
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Creating a set of visited to detect cycle in graph
        visited = set()

        # DFS definition
        def dfs(node, parent):
            visited.add(node)  # we will add node to visited first

            for neighbour in graph[node]:
                if neighbour == parent:
                    continue

                if neighbour in visited:  # we got cycle here
                    return False

                if not dfs(neighbour, node):
                    return False

            return True

        # dfs will start from 0 to find cycles in graph
        if not dfs(0, -1):
            return False

        # to check if all nodes are connected
        return len(visited) == n
