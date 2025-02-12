"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Freckles 2

* Link: https://open.kattis.com/contests/oxdzcd/submissions/15126012

* @Author Mohamed Osman 

* @Team : MO

* Method : Kruskal's Algorithm for Minimum Spanning Tree (O(E log E) with Union-Find)

* Status : Time Limit Exceeded 

* Runtime: > 2.00 s 
"""

import math

def compute_minimum_ink(n, freckles):
    def euclidean_distance(p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(freckles[i], freckles[j])
            edges.append((dist, i, j))
    
    edges.sort()

    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

    total_cost = 0
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            total_cost += dist

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
            index += 1
        n = int(data[index])
        index += 1
        freckles = []
        for _ in range(n):
            x, y = map(float, data[index].split())
            freckles.append((x, y))
            index += 1
        results.append(f"{compute_minimum_ink(n, freckles):.2f}")
    
    print("\n\n".join(results))
