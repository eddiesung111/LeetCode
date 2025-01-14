class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        result = 0
        for length in range(n):
            for start in range(n):
                end = start + length
                if end >= n:
                    break
    
                zero_occur = 0
                for idx in range(start, end+1):
                    print(s[idx])
                    if s[idx] == '0':
                        zero_occur += 1
                one_occur = length - zero_occur + 1

                if k >= zero_occur or k >= one_occur:
                    result += 1
        
        return result
