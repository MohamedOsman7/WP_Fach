"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Locked Treasure 

* Link: https://open.kattis.com/contests/iju6a9/problems/lockedtreasure

* @Author Mohamed Osman 

* @Team : MO

* Method : Combinatorics (Binomial Coefficient Calculation, O(1) using factorial formula)

* Status : Accepted 

* Runtime: ~ 0.000071 s 
"""

import math

def min_locks_needed(n, m):
    return math.comb(n, m)

test_data = [
    """4
3 2
5 1
10 7
5 3"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    T = int(lines[0].strip())
    for i in range(1, T + 1):
        n, m = map(int, lines[i].strip().split())
        print(min_locks_needed(n, m))
    print()

end_time = time.time()
print(f"Runtime: {end_time - start_time:.6f} s")
