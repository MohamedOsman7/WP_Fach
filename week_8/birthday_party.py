"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Birthday Party

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199099

* @Author Mohamed Osman 

* @Team : MO

* Method : Graph Traversal using Tarjan's Algorithm for Bridge Finding (O(P + C))

* Status : Accepted 

* Runtime: 0.06 s 
"""

from collections import defaultdict

def is_critical_connection(p, connections):
    def dfs(node, parent, time):
        nonlocal timer
        visited[node] = True
        discovery[node] = timer
        low[node] = timer
        timer += 1

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if not visited[neighbor]:
                dfs(neighbor, node, time + 1)
                low[node] = min(low[node], low[neighbor])
                if low[neighbor] > discovery[node]:
                    bridges.append((node, neighbor))
            else:
                low[node] = min(low[node], discovery[neighbor])

    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * p
    discovery = [-1] * p
    low = [-1] * p
    timer = 0
    bridges = []

    for i in range(p):
        if not visited[i]:
            dfs(i, -1, 0)

    return len(bridges) > 0

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    results = []
    i = 0
    while i < len(data):
        line = data[i]
        i += 1
        if line == "0 0":
            break
        p, c = map(int, line.split())
        connections = []
        for _ in range(c):
            a, b = map(int, data[i].split())
            connections.append((a, b))
            i += 1

        if is_critical_connection(p, connections):
            results.append("Yes")
        else:
            results.append("No")

    sys.stdout.write("\n".join(results) + "\n")
