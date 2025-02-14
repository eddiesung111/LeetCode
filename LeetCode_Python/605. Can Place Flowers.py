class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Time = O(n)
        # Space = O(1)
        for i in range(len(flowerbed)):
            left = flowerbed[max(0,i-1)]
            right = flowerbed[min(len(flowerbed) - 1, i+1)]
            if left == 0 and right == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        return n <= 0
