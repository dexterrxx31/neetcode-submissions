class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, idx):
            if len(word) == idx:
                return True

            if not (0 <= row < rows and 0 <= col < cols and board[row][col] == word[idx]):
                return False

            original = board[row][col]
            board[row][col] = "#"

            finding = (
                dfs(row + 1, col, idx + 1)
                or dfs(row, col + 1, idx + 1)
                or dfs(row - 1, col, idx + 1)
                or dfs(row, col - 1, idx + 1)
            )
            board[row][col] = original
            return finding

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True

        return False
