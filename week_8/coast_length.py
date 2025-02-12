"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Coast Length

* Link: https://open.kattis.com/contests/m68tjy/submissions/15198077

* @Author Mohamed Osman 

* @Team : MO

* Method : Breadth-First Search (BFS) for Water Expansion & Grid Traversal (O(n*m))

* Status : Accepted 

* Runtime: 0.40 s 
"""

from collections import deque

def calculate_coast_length(grid, n, m):
    def is_within_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        if grid[i][0] == 0:
            queue.append((i, 0))
            visited[i][0] = True
        if grid[i][m - 1] == 0:
            queue.append((i, m - 1))
            visited[i][m - 1] = True
    for j in range(m):
        if grid[0][j] == 0:
            queue.append((0, j))
            visited[0][j] = True
        if grid[n - 1][j] == 0:
            queue.append((n - 1, j))
            visited[n - 1][j] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_within_bounds(nx, ny) and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    coast_length = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if not is_within_bounds(nx, ny) or (is_within_bounds(nx, ny) and visited[nx][ny]):
                        coast_length += 1
    return coast_length

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    grid = [list(map(int, line)) for line in data[1:]]
    
    print(calculate_coast_length(grid, n, m))
