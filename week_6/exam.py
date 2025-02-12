"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Exam

* Link: https://open.kattis.com/contests/uaitfj/submissions/15075707

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy Approach (Counting Matches and Adjustments, O(n))

* Status : Accepted 

* Runtime: 0.04 s 
"""

def max_possible_score(k, my_answers, friend_answers):
    n = len(my_answers)
    matching = sum(1 for i in range(n) if my_answers[i] == friend_answers[i])
    differing = n - matching

    max_score = min(k, matching) + min(differing, n - k)
    return max_score


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    k = int(data[0])
    my_answers = data[1]
    friend_answers = data[2]
    print(max_possible_score(k, my_answers, friend_answers))
