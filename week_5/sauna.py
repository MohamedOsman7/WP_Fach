"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Sauna

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007577

* @Author Mohamed Osman 

* @Team : MO

* Method : Interval Intersection (Greedy Approach, O(n))

* Status : Accepted 

* Runtime: 0.15 s
"""
def sauna_temperature(n, ranges):
    min_temp = 0
    max_temp = 2 * 10**5

    for a, b in ranges:
        min_temp = max(min_temp, a)
        max_temp = min(max_temp, b)

        if min_temp > max_temp:
            print("bad news")
            return
    
    count = max_temp - min_temp + 1
    print(count, min_temp)

# Input 1
# n = 3
# ranges = [
#     (70000, 70005),
#     (70003, 70010),
#     (65000, 80000)
# ]
# sauna_temperature(n, ranges)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])
    
    ranges = [tuple(map(int, line.split())) for line in data[1:]]
    
    sauna_temperature(n, ranges)