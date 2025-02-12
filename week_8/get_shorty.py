"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Get Shorty

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199036

* @Author Mohamed Osman 

* @Team : MO

* Method : Dijkstra's Algorithm using Maximum Probability Path (O((N + M) log N))

* Status : Accepted 

* Runtime: 0.34 s 
"""

import heapq

def dijkstra(n, graph):
    max_heap = [(-1.0, 0)]
    probabilities = [0.0] * n
    probabilities[0] = 1.0

    while max_heap:
        current_prob, current_node = heapq.heappop(max_heap)
        current_prob = -current_prob

        if current_prob < probabilities[current_node]:
            continue

        for neighbor, factor in graph[current_node]:
            new_prob = current_prob * factor
            if new_prob > probabilities[neighbor]:
                probabilities[neighbor] = new_prob
                heapq.heappush(max_heap, (-new_prob, neighbor))

    return probabilities[n - 1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    i = 0
    results = []

    while i < len(data):
        line = data[i]
        i += 1
        n, m = map(int, line.split())
        if n == 0 and m == 0:
            break

        graph = [[] for _ in range(n)]
        for _ in range(m):
            x, y, f = data[i].split()
            x, y, f = int(x), int(y), float(f)
            graph[x].append((y, f))
            graph[y].append((x, f))
            i += 1

        result = dijkstra(n, graph)
        results.append(f"{result:.4f}")

    sys.stdout.write("\n".join(results) + "\n")
