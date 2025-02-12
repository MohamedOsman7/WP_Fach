"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Radio Commercials

* Link: https://open.kattis.com/contests/rfq9ju/submissions/15262980

* @Author Mohamed Osman 

* @Team : MO

* Method : Kadane's Algorithm for Maximum Subarray Sum (O(N))

* Status : Accepted 

* Runtime: 0.06 s 
"""

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, P = map(int, data[0].split())
    student_list = list(map(int, data[1].split()))
    
    adjusted_profits = [students - P for students in student_list]
    
    max_current = max_global = adjusted_profits[0]
    
    for i in range(1, N):
        max_current = max(adjusted_profits[i], max_current + adjusted_profits[i])
        max_global = max(max_global, max_current)
    
    print(max_global)

if __name__ == "__main__":
    main()
