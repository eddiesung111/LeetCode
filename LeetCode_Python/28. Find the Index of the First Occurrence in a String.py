class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Time = O(m + n)
        # Space = O(m)
        m = len(haystack)
        n = len(needle)
        prefix_table = [0 for _ in range(n)]
        j = 0
        for idx in range(1, n):
            while j > 0 and needle[idx] != needle[j]:
                j = prefix_table[j - 1]
            
            if needle[idx] == needle[j]:
                j += 1
                prefix_table[idx] = j
        pos = 0
        for idx in range(m):
            while pos > 0 and haystack[idx] != needle[pos]:
                pos = prefix_table[pos - 1]
            if haystack[idx] == needle[pos]:
                pos += 1
            if pos == n:
                return idx - n + 1
        return -1

    def strStr1(self, haystack: str, needle: str) -> int:
        # Time = O(nm)
        # Space = O(1)
        n = len(needle)
        m = len(haystack)
        for idx in range(m - n + 1):
            if haystack[idx: idx+n] == needle:
                return idx
        return -1
