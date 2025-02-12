"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Catalan Numbers

* Link: https://open.kattis.com/contests/uaitfj/submissions/15075998

* @Author Mohamed Osman 

* @Team : MO

* Method : Dynamic Programming with Binomial Coefficient Formula (O(n))

* Status : Accepted 

* Runtime: 0.08 s 
"""

def compute_catalan_numbers(max_n):
    catalan = [0] * (max_n + 1)
    catalan[0] = 1

    for n in range(1, max_n + 1):
        catalan[n] = catalan[n - 1] * (2 * (2 * n - 1)) // (n + 1)
    
    return catalan


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    q = int(data[0])
    queries = list(map(int, data[1:]))

    max_x = max(queries)
    catalan_numbers = compute_catalan_numbers(max_x)

    for x in queries:
        print(catalan_numbers[x])
