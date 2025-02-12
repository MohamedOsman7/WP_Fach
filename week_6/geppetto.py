"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Geppetto 

* Link: https://open.kattis.com/contests/uaitfj/submissions/15075800

* @Author Mohamed Osman 

* @Team : MO

* Method : Backtracking with Set Pruning (O(2^N))

* Status : Accepted 

* Runtime: 0.72 s 
"""

def count_valid_pizzas(N, M, restrictions):
    restricted_pairs = {frozenset((a - 1, b - 1)) for a, b in restrictions}

    def backtrack(index, active_ingredients):
        if index == N:
            return 1

        total_pizzas = backtrack(index + 1, active_ingredients)

        for other in active_ingredients:
            if frozenset((index, other)) in restricted_pairs:
                break
        else:
            total_pizzas += backtrack(index + 1, active_ingredients | {index})

        return total_pizzas

    return backtrack(0, set())


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, M = map(int, data[0].split())
    restrictions = [tuple(map(int, line.split())) for line in data[1:M + 1]]
    
    print(count_valid_pizzas(N, M, restrictions))
