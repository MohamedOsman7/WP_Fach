"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Prime Reduction 

* Link: https://open.kattis.com/contests/acee7h/problems/primereduction

* @Author Mohamed Osman 

* @Team : MO

* Method : Prime Factorization & Reduction Loop (O(√N) for factorization, repeated)

* Status : Accepted 

* Runtime: ~ 0.000148 s 
"""

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    i = 5
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        while n % (i + 2) == 0:
            factors.append(i + 2)
            n //= (i + 2)
        i += 6
    if n > 1:
        factors.append(n)
    return factors

def prime_reduction(x):
    steps = 0
    while not is_prime(x):
        x = sum(prime_factors(x))
        steps += 1
    return x, steps + 1

# Sample Test Data
test_data = [
    """2
3
5
76
100
2001
4"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    for line in lines:
        x = int(line.strip())
        if x == 4:
            break
        result, steps = prime_reduction(x)
        print(result, steps)
    print()

end_time = time.time()
print(f"Runtime: {end_time - start_time:.6f} s")
