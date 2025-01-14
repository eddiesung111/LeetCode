class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def modify(i, j):
            board[i][j] = "O1"
            if j < n-1 and board[i][j+1] == "O":
                modify(i,j+1)

            if i < m-1 and board[i+1][j] == "O":
                modify(i+1,j)

            if i > 0 and board[i-1][j] == "O":
                modify(i-1,j)

            if j > 0 and board[i][j-1] == "O":
                modify(i,j-1)
            return 
        
        for idx_j in range(n):
            if board[0][idx_j] == "O":
                modify(0, idx_j)

            if board[m-1][idx_j] == "O":
                modify(m-1, idx_j)
        
        for idx_i in range(m):
            if board[idx_i][0] == "O":
                modify(idx_i, 0)

            if board[idx_i][n-1] == "O":
                modify(idx_i, n-1)        
        
        for p in range(m):
            for q in range(n):
                if board[p][q] == "O":
                    board[p][q] = "X"
                elif board[p][q] == "O1":
                    board[p][q] = "O"
