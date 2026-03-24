import sys

input = sys.stdin.readline

x, y = map(int, input().rstrip().split())
k = int(input().rstrip())
nowx = 1
nowy = 0
cnt = 0
if x * y < k:
    print(0)
else:
    while cnt != k:
        for i in range(y):
            if cnt == k:
                break
            nowy += 1
            cnt += 1
        for i in range(x - 1):
            if cnt == k:
                break
            nowx += 1
            cnt += 1
        for i in range(y - 1):
            if cnt == k:
                break
            nowy -= 1
            cnt += 1
        for i in range(x - 2):
            if cnt == k:
                break
            nowx -= 1
            cnt += 1
        x -= 2
        y -= 2
    print(f"{nowx} {nowy}")
