"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Which Number Kind Is It?

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007599

* @Author Mohamed Osman 

* @Team : MO

* Method : Number Classification (Perfect Square Check & Parity, O(1) per number)

* Status : Accepted 

* Runtime: 	0.11 s
"""

import math

def which_number_kind(T, numbers):
    results = []
    for N in numbers:
        is_square = math.isqrt(N)**2 == N
        is_odd = N % 2 == 1

        if is_odd and is_square:
            results.append("OS")
        elif is_odd:
            results.append("O")
        elif is_square:
            results.append("S")
        else:
            results.append("EMPTY")

    for result in results:
        print(result)
        

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    T = int(data[0])
    numbers = list(map(int, data[1:]))

    which_number_kind(T, numbers)