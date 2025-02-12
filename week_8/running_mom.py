"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Running MoM

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199159

* @Author Mohamed Osman 

* @Team : MO

* Method : Tarjan's Algorithm for Strongly Connected Components (SCC) & BFS for Reachability

* Status : Accepted 

* Runtime: 0.07 s
"""

from collections import defaultdict, deque

def find_safety_status(flight_routes, cities_to_check):
    graph = defaultdict(list)
    for src, dest in flight_routes:
        graph[src].append(dest)

    def find_strongly_connected_components():
        index = 0
        stack = []
        indices = {}
        lowlink = {}
        on_stack = set()
        scc = []

        def strongconnect(node):
            nonlocal index
            indices[node] = lowlink[node] = index
            index += 1
            stack.append(node)
            on_stack.add(node)

            for neighbor in graph[node]:
                if neighbor not in indices:
                    strongconnect(neighbor)
                    lowlink[node] = min(lowlink[node], lowlink[neighbor])
                elif neighbor in on_stack:
                    lowlink[node] = min(lowlink[node], indices[neighbor])

            if lowlink[node] == indices[node]:
                component = []
                while True:
                    w = stack.pop()
                    on_stack.remove(w)
                    component.append(w)
                    if w == node:
                        break
                scc.append(component)

        for node in list(graph.keys()):
            if node not in indices:
                strongconnect(node)

        return scc

    sccs = find_strongly_connected_components()

    safe_cities = set()
    for component in sccs:
        if len(component) > 1:
            safe_cities.update(component)

    def is_safe(city):
        if city in safe_cities:
            return True
        visited = set()
        queue = deque([city])
        while queue:
            current = queue.popleft()
            if current in safe_cities:
                return True
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    result = []
    for city in cities_to_check:
        if is_safe(city):
            result.append(f"{city} safe")
        else:
            result.append(f"{city} trapped")

    return result


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    flight_routes = []
    i = 1
    while i <= n:
        src, dest = data[i].split()
        flight_routes.append((src, dest))
        i += 1

    cities_to_check = data[i:]
    results = find_safety_status(flight_routes, cities_to_check)
    sys.stdout.write("\n".join(results) + "\n")
