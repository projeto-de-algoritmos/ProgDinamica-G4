from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        distances = [[float('inf')] * n for _ in range(n)]

        for u, v, w in edges:
            distances[u][v] = w
            distances[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]

        reachable_cities = [0] * n
        for i in range(n):
            for j in range(n):
                if i != j and distances[i][j] <= distanceThreshold:
                    reachable_cities[i] += 1

        min_reachable = float('inf')
        city_index = -1
        for i in range(n):
            if reachable_cities[i] <= min_reachable:
                min_reachable = reachable_cities[i]
                city_index = i

        return city_index
