class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        low = 0
        high = n - 1
        while low <= high:
            mid = int(low + (high - low) / 2)
            if n - citations[mid] == mid:
                return citations[mid]
            
            elif n - mid > citations[mid]:
                low = mid + 1
            
            else:
                high = mid - 1
            
        return n - low

