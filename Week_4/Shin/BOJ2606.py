import sys

input = sys.stdin.readline

node = int(input())
T = int(input())

arr = [[] for _ in range(node + 1)]

for t in range(T):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [False] * (node + 1)
count = 0


def dfs(cur):
    global count
    for nxt in arr[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            count += 1
            dfs(nxt)


visited[1] = True
dfs(1)

print(count)
