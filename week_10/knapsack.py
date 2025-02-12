"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Knapsack 

* Link: https://open.kattis.com/contests/fo8vwg/problems/knapsack

* @Author Mohamed Osman 

* @Team : MO

* Method : 0/1 Knapsack Dynamic Programming (O(nC))

* Status : Accepted 

* Runtime: ~ 0.000092 s
"""

def knapsack(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(capacity + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    w = capacity
    chosen = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen.append(i - 1)
            w -= items[i - 1][1]
    
    return dp[n][capacity], sorted(chosen)

test_data = [
    """5 3
1 5
10 5
100 5
6 4
5 4
4 3
3 2
2 1"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        capacity, n = map(int, lines[i].split())
        i += 1
        items = []
        for _ in range(n):
            value, weight = map(int, lines[i].split())
            items.append((value, weight))
            i += 1
        
        max_value, chosen_items = knapsack(capacity, items)
        print(len(chosen_items))
        print(*chosen_items)
    print()

end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")
