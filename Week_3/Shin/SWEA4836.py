import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    array = [[0 for i in range(10)] for j in range(10)]
    total = 0
    N = int(input())
    for n in range(N):
        x1, y1, x2, y2, color = map(int, input().rstrip().split())
        for i in range(y1, y2 + 1):
            for j in range(x1, x2 + 1):
                array[i][j] += color
    for i in range(10):
        for j in range(10):
            if array[i][j] == 3:
                total += 1
    print(f"#{t+1} {total}")
