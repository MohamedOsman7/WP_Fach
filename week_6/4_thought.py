"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: 4 thought 

* Link: https://open.kattis.com/contests/uaitfj/submissions/15076520

* @Author Mohamed Osman 

* @Team : MO

* Method : Precompute All Possible Expressions Using Four 4's (O(1) lookup)

* Status : Accepted 

* Runtime: 0.04 s 
"""

from itertools import product

def precompute_solutions():
    operators = ['+', '-', '*', '/']
    solutions = {}

    for ops in product(operators, repeat=3):
        expression = f"4 {ops[0]} 4 {ops[1]} 4 {ops[2]} 4"
        try:
            result = eval(expression.replace('/', '//'))
            if result not in solutions:
                solutions[result] = expression
        except ZeroDivisionError:
            continue

    return solutions


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    m = int(data[0])
    test_cases = list(map(int, data[1:]))

    solutions = precompute_solutions()

    for n in test_cases:
        if n in solutions:
            print(f"{solutions[n]} = {n}")
        else:
            print("no solution")
