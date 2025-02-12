"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: 4 thought 

* Link: https://open.kattis.com/contests/iju6a9/problems/4thought

* @Author Mohamed Osman 

* @Team : MO

* Method : Precompute all possible expressions with four 4's (O(1) lookup)

* Status : Accepted 

* Runtime: ~ 0.000137 s 
"""

from itertools import product

operations = ["+", "-", "*", "//"]
expressions = {}

for op1, op2, op3 in product(operations, repeat=3):
    expr = f"4 {op1} 4 {op2} 4 {op3} 4"
    result = eval(expr.replace("//", "/"))
    if result == int(result):
        expressions[int(result)] = expr.replace("//", "/") + " ="

# Sample Test Data
test_data = [
    """5
9
0
7
11
24"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    T = int(lines[0].strip())
    for i in range(1, T + 1):
        n = int(lines[i].strip())
        if n in expressions:
            print(expressions[n], n)
        else:
            print("no solution")
    print()
    
end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")