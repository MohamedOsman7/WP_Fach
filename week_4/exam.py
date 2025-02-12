"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Exam 

* Link: https://open.kattis.com/contests/iju6a9/problems/exam

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy approach (O(n))

* Status : Accepted 

* Runtime: ~ 0.000108 s 
"""

def max_possible_score(k, your_answers, friend_answers):
    n = len(your_answers)
    correct_matches = sum(1 for i in range(n) if your_answers[i] == friend_answers[i])
    incorrect_matches = n - correct_matches
    return min(correct_matches, k) + min(incorrect_matches, n - k)


test_data = [
    """3
FTFFF
TFTTT""",
    """6
TTFTFFTFTF
TTTTFFTTTT"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    k = int(lines[0].strip())
    your_answers = lines[1].strip()
    friend_answers = lines[2].strip()
    print(max_possible_score(k, your_answers, friend_answers))
    print()

end_time = time.time()
# print(f"Runtime: {end_time - start_time:.6f} s")
