class Solution:
    # Time = O(N^2 * log K)
    # Space = O(K)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        max_heap = []
        heapq.heapify(max_heap)
        size = 0
        for i in range(n):
            for j in range(n):
                heapq.heappush(max_heap, -matrix[i][j])
                size += 1
                if size > k:
                    heapq.heappop(max_heap)
                    size -= 1
        return -max_heap[0]

    # Time = O(NlogD), D = diff(min_element, max_element)
    # Space = O(1)
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def count_less_equal(mid):
            i = n - 1
            j = 0
            count = 0
            while i > 0 and j < n:
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            return count
        
        left = matrix[0][0]
        right = matrix[n-1][n-1]
        while left < right:
            mid = left + (right - left) // 2
            if count_less_equal(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
