class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Time = O(mn)
        # Space = O(1)
        m_length = len(matrix)
        n_length = len(matrix[0])
        m, n = 0, 0
        dm = 0
        dn = 1
        res = []
        for _ in range(m_length * n_length):
            res.append(matrix[m][n])
            matrix[m][n] = "."
            if not 0 <= m + dm <= m_length - 1 or not 0 <= n + dn <= n_length - 1 or matrix[m+dm][n+dn] == '.':
                dn, dm = -dm, dn
            m += dm
            n += dn
        return res
