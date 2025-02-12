"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: The Easiest Problem Is This One 

* Link: https://open.kattis.com/contests/acee7h/problems/easiest

* @Author Mohamed Osman 

* @Team : MO

* Method : Brute Force Iteration (O(N log N) worst case)

* Status : Accepted 

* Runtime: ~ 0.000243 s
"""

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def find_min_p(N):
    target_sum = sum_of_digits(N)
    p = 11  # Start from 11 as per problem constraints
    while True:
        if sum_of_digits(N * p) == target_sum:
            return p
        p += 1

# Sample Test Data
test_data = [
    """3029
4
5
42
0"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    for line in lines:
        N = int(line.strip())
        if N == 0:
            break
        print(find_min_p(N))
    print()

end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")
