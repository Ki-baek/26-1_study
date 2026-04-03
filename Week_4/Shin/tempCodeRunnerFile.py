# 2차원 배열에 index로 연결된 노드 추가
import sys

input = sys.stdin.readline

node = int(input())
T = int(input())

arr = [[] for _ in range(node + 1)]
virus = [0 for _ in range(node + 1)]
virus[1] = 1
for t in range(T):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, node + 1):
    if virus[i] == 1:
        for j in range(len(arr[i])):
            virus[arr[i][j]] = 1
print(virus.count(1) - 1)
