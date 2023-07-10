from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        dist = [float('inf')] * n
        stops = [float('inf')] * n
        dist[src] = 0
        stops[src] = 0

        for _ in range(k + 1):
            updated = False
            for flight in flights:
                from_city, to_city, price = flight
                if dist[from_city] + price < dist[to_city] and stops[from_city] < k + 1:
                    dist[to_city] = dist[from_city] + price
                    stops[to_city] = stops[from_city] + 1
                    updated = True
            if not updated:
                break

        for flight in flights:
            from_city, to_city, price = flight
            if dist[from_city] + price < dist[to_city] and stops[from_city] <= k and stops[to_city] <= k:
                return -1
            
        return dist[dst] if dist[dst] < float('inf') else -1