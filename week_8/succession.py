"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Succession

* Link: https://open.kattis.com/contests/m68tjy/submissions/15199087

* @Author Mohamed Osman 

* @Team : MO

* Method : Graph Traversal with Recursive Bloodline Computation (O(N + M))

* Status : Accepted 

* Runtime: 0.04 s 
"""

from collections import defaultdict

def calculate_bloodline(founder, relations, claimants):
    blood = defaultdict(float)
    blood[founder] = 1.0

    parents = defaultdict(list)
    for child, parent1, parent2 in relations:
        parents[child] = [parent1, parent2]

    for child, parent1, parent2 in relations:
        if parent1 not in blood:
            blood[parent1] = 0.0
        if parent2 not in blood:
            blood[parent2] = 0.0
        if child not in blood:
            blood[child] = 0.0

    def compute_blood(person):
        if person not in parents:
            return blood[person]
        if blood[person] > 0:
            return blood[person]
        parent1, parent2 = parents[person]
        blood[person] = (compute_blood(parent1) + compute_blood(parent2)) / 2.0
        return blood[person]

    for claimant in claimants:
        compute_blood(claimant)

    best_claimant = max(claimants, key=lambda c: blood[c])
    return best_claimant

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    results = []
    i = 0
    while i < len(data):
        if data[i].strip() == "":
            i += 1
            continue

        n, m = map(int, data[i].split())
        i += 1
        founder = data[i]
        i += 1
        relations = []
        for _ in range(n):
            child, parent1, parent2 = data[i].split()
            relations.append((child, parent1, parent2))
            i += 1
        claimants = []
        for _ in range(m):
            claimants.append(data[i])
            i += 1

        result = calculate_bloodline(founder, relations, claimants)
        results.append(result)

    sys.stdout.write("\n".join(results) + "\n")
