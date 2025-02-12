"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Freckles

* Link: https://open.kattis.com/contests/m68tjy/submissions/15198067

* @Author Mohamed Osman 

* @Team : MO

* Method : Prim's Algorithm with Min-Heap (O(E log V))

* Status : Accepted 

* Runtime: 1.16 s 
"""

import math
from heapq import heappop, heappush

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def prim_minimum_spanning_tree(points):
    n = len(points)
    visited = [False] * n
    min_heap = [(0, 0)]  # (cost, point_index)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, u = heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_cost += cost
        edges_used += 1

        for v in range(n):
            if not visited[v]:
                dist = calculate_distance(points[u], points[v])
                heappush(min_heap, (dist, v))

    return total_cost

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0
    t = int(data[i])
    i += 1
    results = []
    while t > 0:
        t -= 1
        i += 1
        n = int(data[i])
        i += 1
        points = []
        for _ in range(n):
            x, y = map(float, data[i].split())
            points.append((x, y))
            i += 1
        result = prim_minimum_spanning_tree(points)
        results.append(f"{result:.2f}")
    
    sys.stdout.write("\n\n".join(results) + "\n")
