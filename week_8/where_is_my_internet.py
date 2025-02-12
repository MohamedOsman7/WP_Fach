"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Where's My Internet??

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199186

* @Author Mohamed Osman 

* @Team : MO

* Method : Breadth-First Search (BFS) for Graph Connectivity Check (O(N + M))

* Status : Accepted 

* Runtime: 0.30 s 
"""

from collections import defaultdict, deque

def find_unconnected_houses(n, connections):
    graph = defaultdict(list)
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    connected = set()
    queue = deque([1])
    while queue:
        house = queue.popleft()
        if house in connected:
            continue
        connected.add(house)
        for neighbor in graph[house]:
            if neighbor not in connected:
                queue.append(neighbor)

    unconnected = [i for i in range(1, n + 1) if i not in connected]
    return unconnected

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n, m = map(int, data[0].split())
    connections = [tuple(map(int, line.split())) for line in data[1:m + 1]]

    unconnected_houses = find_unconnected_houses(n, connections)
    if not unconnected_houses:
        print("Connected")
    else:
        print("\n".join(map(str, sorted(unconnected_houses))))
