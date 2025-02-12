"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Minimum Spanning Tree

* Link: https://open.kattis.com/contests/m68tjy/submissions/15198047

* @Author Mohamed Osman 

* @Team : MO

* Method : Kruskal's Algorithm with Union-Find (O(E log E))

* Status : Accepted 

* Runtime: 0.86 s 
"""

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1
        return True
    return False

def kruskal(n, edges):
    parent = [i for i in range(n)]
    rank = [0] * n
    edges.sort(key=lambda x: (x[2], x[0], x[1]))
    mst = []
    total_cost = 0
    for u, v, w in edges:
        if union(parent, rank, u, v):
            mst.append((min(u, v), max(u, v)))
            total_cost += w
    if len(mst) != n - 1:
        return "Impossible"
    mst.sort()
    return total_cost, mst

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    i = 0
    result = []
    while i < len(data):
        line = data[i]
        i += 1
        if line == "0 0":
            break
        n, m = map(int, line.split())
        edges = []
        for _ in range(m):
            u, v, w = map(int, data[i].split())
            i += 1
            edges.append((u, v, w))
        res = kruskal(n, edges)
        if res == "Impossible":
            result.append("Impossible")
        else:
            total_cost, mst = res
            result.append(str(total_cost))
            for u, v in mst:
                result.append(f"{u} {v}")
    sys.stdout.write("\n".join(result) + "\n")
