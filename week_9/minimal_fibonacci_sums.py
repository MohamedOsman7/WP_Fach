"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Minimal Fibonacci Sums

* Link: https://open.kattis.com/contests/rfq9ju/submissions/15255653

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy Algorithm (Zeckendorf's Theorem, O(log n))

* Status : Accepted 

* Runtime: 0.04 s 
"""

def generate_fibonacci_up_to(n):
    fibonacci = [1, 2]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci[:-1]  # Exclude the last number that exceeds n

def minimal_fibonacci_sum(n):
    fibonacci = generate_fibonacci_up_to(n)
    result = []

    # Start from the largest Fibonacci number and work backwards
    for num in reversed(fibonacci):
        if num <= n:
            result.append(num)
            n -= num

    return sorted(result)  # Return the result in increasing order

def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print(" ".join(map(str, minimal_fibonacci_sum(n))))

if __name__ == "__main__":
    main()
