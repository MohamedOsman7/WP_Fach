"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Coast Length

* Link: https://open.kattis.com/contests/oxdzcd/submissions/15126027

* @Author Mohamed Osman 

* @Team : MO

* Method : Breadth-First Search (BFS) for Water Expansion & Grid Traversal (O(n*m))

* Status : Accepted 

* Runtime: 0.32 s 
"""

from collections import deque

def calculate_coast_length(grid, n, m):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    coast_length = 0
    
    def is_water_connected_to_edge(x, y):
        queue = deque([(x, y)])
        visited[x][y] = True
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if grid[nx][ny] == "0" and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
    
    def calculate_coast_for_land():
        nonlocal coast_length
        for x in range(n):
            for y in range(m):
                if grid[x][y] == "1":
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or nx >= n or ny < 0 or ny >= m or grid[nx][ny] == "0" and visited[nx][ny]:
                            coast_length += 1

    for y in range(m):
        if grid[0][y] == "0" and not visited[0][y]:
            is_water_connected_to_edge(0, y)
        if grid[n-1][y] == "0" and not visited[n-1][y]:
            is_water_connected_to_edge(n-1, y)

    for x in range(n):
        if grid[x][0] == "0" and not visited[x][0]:
            is_water_connected_to_edge(x, 0)
        if grid[x][m-1] == "0" and not visited[x][m-1]:
            is_water_connected_to_edge(x, m-1)

    calculate_coast_for_land()
    return coast_length


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    grid = data[1:]
    print(calculate_coast_length(grid, n, m))
