"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Simple Addition 

* Link: https://open.kattis.com/contests/eo92fp/problems/simpleaddition

* @Author Mohamed Osman 

* @Team : MO

* Method : Big Integer Addition

* Status : Accepted 

* Runtime: ~ 0.000041 s 
"""

test_data = [
    """1337
42""",
    """1
9999999999999"""
]

import time

start_time = time.time()

for data in test_data:
    lines = data.split("\n")
    a = int(lines[0].strip())
    b = int(lines[1].strip())
    print(a + b)

end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")
