class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time = O(n)
        # Space = O(n)
        if len(s) != len(t):
            return False
        count = Counter(s)
        for char in t:
            if char not in count or count[char] == 0:
                return False
            else:
                count[char] -= 1
        return True
