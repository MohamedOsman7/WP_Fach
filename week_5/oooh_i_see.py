"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Oooh I See

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007668

* @Author Mohamed Osman 

* @Team : MO

* Method : Grid Search with 8-Direction Adjacency Check (O(r * c))

* Status : Accepted 

* Runtime: 0.05 s 
"""

def find_treasure(r, c, grid):
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    def is_treasure(i, j):
        if grid[i][j] != '0':
            return False
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= r or nj < 0 or nj >= c or grid[ni][nj] != 'O':
                return False
        return True

    treasures = []
    for i in range(1, r - 1):
        for j in range(1, c - 1):
            if is_treasure(i, j):
                treasures.append((i + 1, j + 1))

    if len(treasures) == 0:
        print("Oh no!")
    elif len(treasures) > 1:
        print(f"Oh no! {len(treasures)} locations")
    else:
        print(f"{treasures[0][0]} {treasures[0][1]}")


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    r, c = map(int, data[0].split())
    grid = data[1:]
    find_treasure(r, c, grid)