class Solution:
    def reverseVowels(self, s: str) -> str:
        # Time = O(n)
        # Space = O(n)
        left = 0
        right = len(s) - 1
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', "E", "I", "O", "U"])
        s = list(s)
        while left < right:
            while left < right and s[left] not in vowel_set:
                left += 1
            while left < right and s[right] not in vowel_set:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
