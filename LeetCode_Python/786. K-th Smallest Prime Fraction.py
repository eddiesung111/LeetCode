class Solution:
    # Time = O(nlogn)
    # Space = O(1)
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        def search(mid):
            count = 0
            max_fraction = 0
            last_i, last_j = 0, 0
            j = 0

            for i in range(n):
                while j < n and arr[i] >= mid * arr[j]:
                    j += 1
                count += n - j
                if j < n and i < j and arr[i] > max_fraction * arr[j]:
                    max_fraction = arr[i] / arr[j]
                    last_i, last_j = i, j
            return count, last_i, last_j

        left, right = 0, 1
        while left < right:
            mid = (left + right) / 2
            count, idx_i, idx_j = search(mid)
            if count == k:
                return [arr[idx_i], arr[idx_j]]
            elif count < k:
                left = mid
            else:
                right = mid

    

    # Time = O(n^2 * logk)
    # Space = O(k)
    def kthSmallestPrimeFraction2(self, arr: List[int], k: int) -> List[int]:
        max_heap = []
        heapq.heapify(max_heap)
        n = len(arr)
        size = 0
        for i in range(n-1):
            for j in range(i+1,n):
                heapq.heappush(max_heap, (-arr[i]/arr[j], arr[i], arr[j]))
                size += 1
                if size > k:
                    heapq.heappop(max_heap)
                    size -= 1
        return [max_heap[0][1], max_heap[0][2]]
