class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Time = O(n)
        # Space = O(n)
        max_cand = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_cand:
                candies[i] = True
            else:
                candies[i] = False
        return candies
