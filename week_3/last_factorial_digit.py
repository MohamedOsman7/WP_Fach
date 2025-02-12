"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Last Factorial Digit 

* Link: https://open.kattis.com/contests/acee7h/problems/lastfactorialdigit

* @Author Mohamed Osman 

* @Team : MO

* Method : Precomputed last digits of factorial (O(1) lookup)

* Status : Accepted 

* Runtime: ~ 0.000119 s 
"""

factorial_last_digit = [1, 1, 2, 6, 4, 0, 0, 0, 0, 0, 0]

# Sample Test Data
test_data = [
    """3
1
2
3""",
    """2
5
2"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    T = int(lines[0].strip())
    for i in range(1, T + 1):
        N = int(lines[i].strip())
        print(factorial_last_digit[N])
    print()  # Blank line for separation

end_time = time.time()
# print(f"Runtime: {end_time - start_time:.6f} s")
