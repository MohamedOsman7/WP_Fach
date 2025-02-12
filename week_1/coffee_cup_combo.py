"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Coffee Cup Combo 

* Link: https://open.kattis.com/contests/v499w5/problems/coffeecupcombo

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy approach, single pass (O(n)) 

* Status : Accepted 

* Runtime: ~ 0.000059 s
"""
import time

def max_awake_lectures(n, s):
    coffee_cups = 0
    awake_lectures = 0

    for lecture in s:
        if lecture == '1':
            awake_lectures += 1
            coffee_cups = 2
        elif coffee_cups > 0:
            awake_lectures += 1
            coffee_cups -= 1

    return awake_lectures


start_time = time.time()
print(max_awake_lectures(10, "0100010100"))  # 8
print(max_awake_lectures(10, "1100000000"))  # 4
print(max_awake_lectures(1, "0"))  # 0
end_time = time.time()

# Approximate runtime calculation

runtime = end_time - start_time
#print(f"Runtime: {runtime:.6f} s")
