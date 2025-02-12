"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Arctic Network

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199165

* @Author Mohamed Osman 

* @Team : MO

* Method : Kruskal's Algorithm for Minimum Spanning Tree (O(E log E))

* Status : Accepted 

* Runtime: 0.81 s 
"""

import math

def calculate_min_d(satellites, outposts):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    edges = []
    for i in range(len(outposts)):
        for j in range(i + 1, len(outposts)):
            d = distance(outposts[i], outposts[j])
            edges.append((d, i, j))

    edges.sort()

    parent = list(range(len(outposts)))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    mst_edges = []
    for d, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append(d)

    mst_edges.sort(reverse=True)
    return mst
