class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Time = O(n * 4^n), n = length of the digits given
        # Space = O(n * 4^n)
        res = ['']
        letters = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        for digit in digits:
            res = [prefix + letter for prefix in res for letter in letters[digit]]
        return res
