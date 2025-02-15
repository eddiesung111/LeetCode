class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # Time = O(mn)
        # Space = O(mn)
        '''
        seen record the number sum we have seen before.
        The position of bit means the sum.  
        eg. 
        00010, it means 1
        0100010 it means 1 and 5
        Afterwards, we push the bit backwards, which represents we add the value.
        00010 << 3 = 010000 [push backward 3 digits]
        Thus, it represents 1 + 3 = 4.
        Therefore, we use seen to record all the sum we have seen on last row.
        new_seen = new_seen | (seen << num), we add each num with seen and record it with OR[|] operation
        Then, we get our new_seen, ie. seen = new_seen.
        We now renew the new_seen and continue the above procedures.
        Then, find the minimum absolute difference.
        '''
        seen = 1
        for row in mat:
            new_seen = 0
            for num in row:
                new_seen = new_seen | (seen << num)
            seen = new_seen
        for i in range(target + 1):
            if seen & (1 << target + i | 1 << target - i): # != 0
                return i
        for i in range(target + 1, 70 * 70 + 1): 
            if seen & (1 << target + i): # != 0
                return i
        
    def minimizeTheDifference2(self, mat: List[List[int]], target: int) -> int:
        # Time = O(m^n)
        # Space = O(n+m)
        m = len(mat)
        n = len(mat[0])
        current_sum = [0]
        for i in range(m):
            next_sum = set()
            for j in range(n):
                for curr in current_sum:
                    next_sum.add(curr + mat[i][j])
            current_sum = next_sum
        return min(abs(target - element) for element in current_sum)
