class Solution:
    # Time = O(log(mn))
    # Space = O(1)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row_left = 0
        row_right = m - 1
        while row_left < row_right:
            row_mid = int(row_left + (row_right - row_left) / 2)
            if matrix[row_mid][-1] == target:
                return True
            elif matrix[row_mid][-1] < target:
                row_left = row_mid + 1
            else:
                row_right = row_mid
        row = row_left
        col_left = 0
        col_right = n - 1
        while col_left < col_right:
            col_mid = int(col_left + (col_right - col_left) / 2)
            if matrix[row][col_mid] == target:
                return True
            elif matrix[row][col_mid] < target:
                col_left = col_mid + 1
            else:
                col_right = col_mid
        col = col_left
        return True if matrix[row][col] == target else False
