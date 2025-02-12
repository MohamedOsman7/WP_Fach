"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Guess the Number 

* Link: https://open.kattis.com/contests/eo92fp/problems/guess

* @Author Mohamed Osman 

* @Team : MO

* Method : Binary Search (O(log N))

* Status : Accepted 

* Runtime: 0 s 
"""

def guess_the_number():
    low, high = 1, 1000

    while low <= high:
        guess = (low + high) // 2
        print(guess)
        
        response = input()
        
        if response == "correct":
            break
        elif response == "lower":
            high = guess - 1
        elif response == "higher":
            low = guess + 1

guess_the_number()
