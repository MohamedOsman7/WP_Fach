"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Exact Change 

* Link: https://open.kattis.com/contests/fo8vwg/problems/exactchange2

* @Author Mohamed Osman 

* @Team : MO

* Method : Dynamic Programming (Coin Change, O(nC))

* Status : Accepted 

* Runtime: ~ 0.001138 s 
"""

def exact_change(price, coins):
    max_value = sum(coins) + 1
    dp = [float('inf')] * max_value
    dp[0] = 0
    
    for coin in coins:
        for j in range(max_value - 1, coin - 1, -1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
    
    for total_paid in range(price, max_value):
        if dp[total_paid] != float('inf'):
            return total_paid, dp[total_paid]
    
    return -1, -1

test_data = [
    """1
1400
3
500
1000
2000"""
]

import time
start_time = time.time()

for index, data in enumerate(test_data, 1):
    print(f"Sample {index} result:")
    lines = data.split("\n")
    T = int(lines[0].strip())
    i = 1
    for _ in range(T):
        price = int(lines[i].strip())
        i += 1
        n = int(lines[i].strip())
        i += 1
        coins = [int(lines[j].strip()) for j in range(i, i + n)]
        i += n
        total_paid, num_coins = exact_change(price, coins)
        print(total_paid, num_coins)
    print()

end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")
