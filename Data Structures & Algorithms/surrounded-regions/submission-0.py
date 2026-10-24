class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols):
                return

            if board[r][c] != "O":
                return

            board[r][c] = "S"

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"
