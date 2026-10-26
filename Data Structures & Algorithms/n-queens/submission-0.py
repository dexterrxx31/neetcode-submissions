class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result, queen = [], [-1] * n

        def is_safe(row, col):
            for r in range(row):
                if queen[r] == col:
                    return False
                if abs(row - r) == abs(col - queen[r]):
                    return False
            return True

        def bt(row):
            if row == n:
                board = []
                for r in range(n):
                    row_string = "." * queen[r] + "Q" + "." * (n - queen[r] - 1)
                    board.append(row_string)
                result.append(board)
                return

            for col in range(n):
                if not is_safe(row, col):
                    continue

                queen[row] = col
                bt(row + 1)

                queen[row] = -1

        bt(0)
        return result
