class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def validation(input1):
            arr, pos = input1
            length = len(arr)

            if pos == 0 or pos + length >= n:
                return input1

            elif s[pos - 1] != s[pos + length]:
                return input1
            
            new_arr = s[pos - 1 :pos + length + 1]
            pos -= 1
            new_input = (new_arr, pos)
            return validation(new_input)

        odd_input = [(s[idx],idx) for idx in range(n)]
        even_input = [(s[idx:idx+2],idx) for idx in range(n-1) if s[idx] == s[idx+1]]

        odd_output = [validation(item) for item in odd_input]
        even_output = [validation(item) for item in even_input]

        fun = lambda x: len(x[0])
        longest = max(odd_output + even_output, key=fun, default=("None", -1))
        return longest[0]
