"""
Ausgewählte Probleme aus dem ACM Programming Contest  WiSe 2024/2025

* Problem: Image Processing 

* Link: https://open.kattis.com/contests/eo92fp/problems/imageprocessing

* @Author Mohamed Osman 

* @Team : MO

* Method : 2D Convolution with Explicit Kernel Flipping (O(H * W * N * M))

* Status : Accepted 

* Runtime: ~ 0.000048 s 
"""

import time

def apply_convolution(H, W, N, M, image, kernel):
    output_height = H - N + 1
    output_width = W - M + 1
    result = [[0] * output_width for _ in range(output_height)]

    flipped_kernel = [[kernel[N - 1 - i][M - 1 - j] for j in range(M)] for i in range(N)]

    for i in range(output_height):
        for j in range(output_width):
            sum_value = 0
            for ki in range(N):
                for kj in range(M):
                    sum_value += image[i + ki][j + kj] * flipped_kernel[ki][kj]
            result[i][j] = sum_value

    return result

# Simulate unput data
test_data = """4 4 2 2
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
1 2
3 4""".split("\n")


H, W, N, M = map(int, test_data[0].split())
image = [list(map(int, test_data[i + 1].split())) for i in range(H)]
kernel = [list(map(int, test_data[i + 1 + H].split())) for i in range(N)]


start_time = time.time()


result = apply_convolution(H, W, N, M, image, kernel)
for row in result:
    print(*row)


end_time = time.time()
#print(f"Runtime: {end_time - start_time:.6f} s")
