class Solution:
    # Time = O(9^81)
    # Space = O(81) = O(1)
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(map(str, range(1, 10))) for _ in range(9)]
        col = [set(map(str, range(1, 10))) for _ in range(9)]
        box = [set(map(str, range(1, 10))) for _ in range(9)]
        available = (row, col, box)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].remove(board[i][j])
                    col[j].remove(board[i][j])
                    pos_i = i // 3
                    pos_j = j // 3
                    box[pos_i * 3 + pos_j].remove(board[i][j])

        def dfs(pos_i, pos_j, available, board):
            row, col, box = available
            box_pos = pos_i // 3 * 3 + pos_j // 3
            if pos_i == 9:
                return True

            elif pos_j == 8:
                npos_i = pos_i + 1
                npos_j = 0
            else:
                npos_i = pos_i
                npos_j = pos_j + 1

            if board[pos_i][pos_j] != '.':
                return dfs(npos_i, npos_j, available, board)
            else:
                intersect = row[pos_i] & col[pos_j] & box[box_pos]
                if not intersect:
                    return False
                
                else:
                    for value in intersect:
                        board[pos_i][pos_j] = value
                        row[pos_i].remove(value)
                        col[pos_j].remove(value)
                        box[box_pos].remove(value)
                        if dfs(npos_i, npos_j, available, board) == True:
                            return True

                        board[pos_i][pos_j] = "."
                        row[pos_i].add(value)
                        col[pos_j].add(value)
                        box[box_pos].add(value)

        dfs(0, 0, available, board)
