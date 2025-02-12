"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Broken Swords 

* Link: https://open.kattis.com/contests/v499w5/problems/brokenswords

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy approach with counting (O(N))

* Status : Accepted 

* Runtime: ~ 0.000035 s 
"""
import time

def broken_swords(n, slats):
    top_count, bottom_count = 0, 0
    left_count, right_count = 0, 0

    for slat in slats:
        if slat[0] == '1':  # Top (T)
            top_count += 1
        if slat[1] == '1':  # Bottom (B)
            bottom_count += 1
        if slat[2] == '1':  # Left (L)
            left_count += 1
        if slat[3] == '1':  # Right (R)
            right_count += 1

    # Total available T/B and L/R slats
    total_TB = top_count + bottom_count
    total_LR = left_count + right_count

    # Maximum swords we can form
    swords_made = min(total_TB // 2, total_LR // 2)

    # Remaining slats after forming swords
    remaining_TB = total_TB - (swords_made * 2)
    remaining_LR = total_LR - (swords_made * 2)

    return swords_made, remaining_TB, remaining_LR


start_time = time.time()
print(*broken_swords(4, ["0100", "0010", "0110", "1010"]))
end_time = time.time()

# Approximate runtime calculation

runtime = end_time - start_time
#print(f"Runtime: {runtime:.6f} s")
