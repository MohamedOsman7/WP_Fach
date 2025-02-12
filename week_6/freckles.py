"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Freckles

* Link: https://open.kattis.com/contests/uaitfj/submissions/15076408

* @Author Mohamed Osman 

* @Team : MO

* Method : Prim's Algorithm for Minimum Spanning Tree (O(n²) adjacency matrix implementation)

* Status : Time Limit Exceeded 

* Runtime: > 2.00 s 
"""

import math
from heapq import heappush, heappop

def compute_minimum_ink(n, freckles):
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    visited = [False] * n
    min_heap = [(0, 0)]  # (distance, node)
    total_cost = 0

    while min_heap:
        cost, node = heappop(min_heap)
        if visited[node]:
            continue
        visited[node] = True
        total_cost += cost

        for neighbor in range(n):
            if not visited[neighbor]:
                dist = euclidean_distance(freckles[node], freckles[neighbor])
                heappush(min_heap, (dist, neighbor))

    return total_cost


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        while index < len(data) and data[index].strip() == "":
     
