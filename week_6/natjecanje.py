"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Natjecanje

* Link: https://open.kattis.com/contests/uaitfj/submissions/15075729

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy Approach with Set Operations (O(N log N))

* Status : Accepted 

* Runtime: 0.04 s 
"""

def minimal_teams_cannot_start(N, S, R, damaged, reserve):
    damaged_set = set(damaged)
    reserve_set = set(reserve)

    self_help = damaged_set & reserve_set
    damaged_set -= self_help
    reserve_set -= self_help

    for team in sorted(reserve_set):
        if team - 1 in damaged_set:
            damaged_set.remove(team - 1)
        elif team + 1 in damaged_set:
            damaged_set.remove(team + 1)

    return len(damaged_set)


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    N, S, R = map(int, data[0].split())
    damaged = list(map(int, data[1].split()))
    reserve = list(map(int, data[2].split()))
    
    print(minimal_teams_cannot_start(N, S, R, damaged, reserve))
