"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Honeycomb Walk 

* Link: https://open.kattis.com/contests/uaitfj/submissions/15075667

* @Author Mohamed Osman 

* @Team : MO

* Method : Depth-First Search (DFS) with Memoization (O(6^N) reduced with caching)

* Status : Accepted 

* Runtime: 0.08 s 
"""

def honeycomb_walk(n):
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1), (1, -1), (-1, 1)
    ]
    memo = {}

    def dfs(x, y, steps):
        if steps == 0:
            return 1 if (x, y) == (0, 0) else 0

        if (x, y, steps) in memo:
            return memo[(x, y, steps)]

        total_ways = 0
        for dx, dy in directions:
            total_ways += dfs(x + dx, y + dy, steps - 1)

        memo[(x, y, steps)] = total_ways
        return total_ways

    return dfs(0, 0, n)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = int(data[i])
        results.append(honeycomb_walk(n))
    
    for result in results:
        print(result)
