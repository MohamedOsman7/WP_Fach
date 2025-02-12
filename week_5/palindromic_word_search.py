"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Palindromic Word Search

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007929

* @Author Mohamed Osman 

* @Team : MO

* Method : Brute Force Search (O(r² * c² * (r + c)), Optimizations Needed)

* Status : Time Limit Exceeded 

* Runtime: > 6.00 s
"""

def is_palindrome(s):
    return s == s[::-1]

def find_largest_palindromic_area(grid, r, c):
    max_area = 0
    for top in range(r):
        for bottom in range(top, r):
            for left in range(c):
                for right in range(left, c):
                    has_horizontal_palindrome = False
                    for i in range(top, bottom + 1):
                        row_segment = grid[i][left:right + 1]
                        if is_palindrome(row_segment):
                            has_horizontal_palindrome = True
                            break

                    has_vertical_palindrome = False
                    for j in range(left, right + 1):
                        column_segment = [grid[i][j] for i in range(top, bottom + 1)]
                        if is_palindrome(column_segment):
                            has_vertical_palindrome = True
                            break

                    if has_horizontal_palindrome and has_vertical_palindrome:
                        area = (bottom - top + 1) * (right - left + 1)
                        max_area = max(max_area, area)

    return max_area


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    r, c = map(int, data[0].split())
    grid = [list(line) for line in data[1:]]
    print(find_largest_palindromic_area(grid, r, c))
