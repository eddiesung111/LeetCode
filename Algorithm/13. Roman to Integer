class Solution:
    def romanToInt(self, s: str) -> int:
        # Time = O(n)
        # Space = O(1)
        letters = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        res = 0
        for a,b in zip(s, s[1:]):
            if letters[a] < letters[b]:
                res -= letters[a]
            else:
                res += letters[a]
        return res + letters[s[-1]]        
