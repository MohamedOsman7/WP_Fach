"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Breaking Bad

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199109

* @Author Mohamed Osman 

* @Team : MO

* Method : Graph Bipartiteness Check using BFS (O(N + M))

* Status : Accepted 

* Runtime: 0.21 s 
"""

from collections import defaultdict, deque

def is_bipartite_and_partition(n, items, edges):
    item_to_id = {item: i for i, item in enumerate(items)}
    id_to_item = {i: item for item, i in item_to_id.items()}

    graph = defaultdict(list)
    for item1, item2 in edges:
        id1, id2 = item_to_id[item1], item_to_id[item2]
        graph[id1].append(id2)
        graph[id2].append(id1)

    colors = [-1] * n

    def bfs(node):
        queue = deque([node])
        colors[node] = 0
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:
                    return False
        return True

    for i in range(n):
        if colors[i] == -1:
            if not bfs(i):
                return "impossible"

    walter = [id_to_item[i] for i in range(n) if colors[i] == 0]
    jesse = [id_to_item[i] for i in range(n) if colors[i] == 1]

    return walter, jesse

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    i = 0
    results = []
    while i < len(data):
        n = int(data[i])
        i += 1
        items = []
        for _ in range(n):
            items.append(data[i].strip())
            i += 1
        m = int(data[i])
        i += 1
        edges = []
        for _ in range(m):
            edges.append(tuple(data[i].split()))
            i += 1

        result = is_bipartite_and_partition(n, items, edges)
        if result == "impossible":
            results.append("impossible")
        else:
            walter, jesse = result
            results.append(" ".join(sorted(walter)))
            results.append(" ".join(sorted(jesse)))

    sys.stdout.write("\n".join(results) + "\n")
