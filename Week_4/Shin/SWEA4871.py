T = int(input())


for t in range(T):
    node, E = map(int, input().split())
    arr = [[] for _ in range(node + 1)]

    for e in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    S, G = map(int, input().split())
    visited = [False] * (node + 1)
    connected = [0]
    if S == G:
        connected[0] = 1

    def dfs(cur):
        for nxt in arr[cur]:
            if nxt == G:
                connected[0] = 1
                break
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)

    visited[S] = True
    dfs(S)

    print(f"#{t+1} {connected[0]}")
