class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c, reachable):
            reachable.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

                if (nr, nc) in reachable:
                    continue

                if heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, reachable)

        for c in range(cols):
            dfs(0, c, pacific)
        for r in range(rows):
            dfs(r, 0, pacific)

        for c in range(cols):
            dfs(rows - 1, c, atlantic)
        for r in range(rows):
            dfs(r, cols - 1, atlantic)

        return [list(cell) for cell in pacific & atlantic]
