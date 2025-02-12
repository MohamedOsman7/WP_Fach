"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Airfare Grants

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007692

* @Author Mohamed Osman 

* @Team : MO

* Method : Greedy Approach (Finding Minimum Price and Capped Reimbursement, O(n))

* Status : Accepted 

* Runtime: 0.04 s 
"""

def calculate_min_net_cost(n, prices):
    max_reported_price = max(prices)
    min_purchased_price = min(prices)

    reimbursement_limit = max_reported_price // 2
    reimbursement = min(reimbursement_limit, min_purchased_price)

    net_cost = min_purchased_price - reimbursement
    return net_cost


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    prices = list(map(int, data[1:]))
    print(calculate_min_net_cost(n, prices))