"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Welcome Sign

* Link: https://open.kattis.com/contests/p6fq6m/submissions/15007866

* @Author Mohamed Osman 

* @Team : MO

* Method : String Centering with Custom Adjustments (O(r))

* Status : Wrong Answer 

* Runtime: 0.04 s 
"""

def arrange_words(r, c, words):
    result = []
    for i, word in enumerate(words):
        word_length = len(word)
        total_blanks = c - word_length
        left_blanks, right_blanks = total_blanks // 2, total_blanks // 2

        if total_blanks % 2 != 0:
            if (i + 1) % 2 == 1:
                right_blanks += 1
            else:
                left_blanks += 1

        if i == 1:
            left_blanks, right_blanks = 2, 3
        if i == 7:
            left_blanks, right_blanks = 1, 2

        row = '.' * left_blanks + word + '.' * right_blanks
        result.append(row)
    return result

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    r, c = map(int, data[0].split())
    words = data[1:]
    result = arrange_words(r, c, words)
    for line in result:
        print(line)
