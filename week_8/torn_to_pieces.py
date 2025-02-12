"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Torn To Pieces

* Link: https://open.kattis.com/contests/m68tjy/submissions/15204287

* @Author Mohamed Osman 

* @Team : MO

* Method : Depth-First Search (DFS) for Pathfinding in an Undirected Graph (O(N + M))

* Status : Accepted 

* Runtime: 0.04 s 
"""

from collections import defaultdict, deque

def find_route(n, connections, start, destination):
    graph = defaultdict(list)
    for connection in connections:
        parts = connection.split()
        station = parts[0]
        neighbors = parts[1:]
        for neighbor in neighbors:
            graph[station].append(neighbor)
            graph[neighbor].append(station)

    def dfs(station, destination, visited, path):
        if station in visited:
            return None
        visited.add(station)
        path.append(station)

        if station == destination:
            return list(path)

        for neighbor in graph[station]:
            result = dfs(neighbor, destination, visited, path)
            if result:
                return result

        path.pop()
        visited.remove(station)
        return None

    visited = set()
    path = []
    result = dfs(start, destination, visited, path)
    if result:
        return " ".join(result)
    else:
        return "no route found"

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    connections = data[1:n+1]
    start, destination = data[n+1].split()

    print(find_route(n, connections, start, destination))
