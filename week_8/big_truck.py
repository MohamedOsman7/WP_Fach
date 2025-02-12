"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Big Truck

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199214

* @Author Mohamed Osman 

* @Team : MO

* Method : Dijkstra's Algorithm with Item Collection Optimization (O((N + M) log N))

* Status : Accepted 

* Runtime: 0.07 s 
"""

import heapq
from collections import defaultdict

def big_truck(n, items, m, roads):
    graph = defaultdict(list)
    for a, b, d in roads:
        graph[a].append((b, d))
        graph[b].append((a, d))

    def dijkstra(start, end):
        pq = [(0, -items[start - 1], start)]
        distances = [float('inf')] * (n + 1)
        max_items = [0] * (n + 1)
        distances[start] = 0
        max_items[start] = items[start - 1]

        while pq:
            dist, neg_items, node = heapq.heappop(pq)
            current_items = -neg_items

            if dist > distances[node]:
                continue

            for neighbor, weight in graph[node]:
                new_dist = dist + weight
                new_items = current_items + items[neighbor - 1]

                if new_dist < distances[neighbor] or (new_dist == distances[neighbor] and new_items > max_items[neighbor]):
                    distances[neighbor] = new_dist
                    max_items[neighbor] = new_items
                    heapq.heappush(pq, (new_dist, -new_items, neighbor))

        return distances[end], max_collected_items[end]

    shortest_distance, max_collected_items = dijkstra(1, n)

    if shortest_distance == float('inf'):
        return "impossible"
    return f"{shortest_distance} {max_collected_items}"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    items = list(map(int, data[1].split()))
    m = int(data[2])
    roads = [tuple(map(int, line.split())) for line in data[3:3 + m]]

    result = big_truck(n, items, m, roads)
    print(result)
