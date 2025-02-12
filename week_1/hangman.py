"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Hangman 

* Link: https://open.kattis.com/contests/v499w5/problems/hangman 

* @Author Mohamed Osman 

* @Team : MO

* Method : Simulation, Set for fast lookups

* Status : Accepted 

* Runtime: ~ 0.000661 s
"""
import time

def hangman_game(word, permutation):
    word_set = set(word)
    guessed = set()
    mistakes = 0
    max_mistakes = 10
    
    for letter in permutation:
        if letter in word_set:
            guessed.add(letter)
            if guessed == word_set:
                return "WIN"
        else:
            mistakes += 1
            if mistakes == max_mistakes:
                return "LOSE"
    
    return "LOSE"

start_time = time.time()
print(hangman_game("HANGMAN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # WIN
print(hangman_game("BANANA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # LOSE
print(hangman_game("RAINBOWS", "USIANBVLOJRKWXZCTQGHPFMYDE"))  # WIN
end_time = time.time()

# Approximate runtime calculation

runtime = end_time - start_time
#print(f"Runtime: {runtime:.6f} s")
