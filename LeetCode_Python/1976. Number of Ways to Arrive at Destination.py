class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Time = O(mlogn), where m is the no. of relations of the road
        # Space = O(m + n)
        graph = defaultdict(list)
        for u, v, cost in roads:
            graph[u].append([v, cost])
            graph[v].append([u, cost])
        min_heap = [(0, 0)] # start, dist
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        while min_heap:
            cost, start = heappop(min_heap)
            if dist[start] < cost:
                continue
            for des, time in graph[start]:
                if dist[des] > cost + time:
                    dist[des] = cost + time
                    ways[des] = ways[start]
                    heappush(min_heap, (dist[des], des))
                elif dist[des] == cost + time:
                    ways[des] = (ways[des] + ways[start]) % 1_000_000_007
        return ways[n - 1]
