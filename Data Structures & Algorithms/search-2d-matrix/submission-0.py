class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        start = 0
        end = (row * col) - 1

        while end >= start:
            mid = (start + end) // 2
            r = mid // col
            c = mid % col

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                start = mid + 1
            elif target < matrix[r][c]:
                end = mid - 1
        return False
