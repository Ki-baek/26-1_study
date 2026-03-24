import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    P, pa, pb = map(int, input().rstrip().split())
    cnta = 0
    cntb = 0

    l = 1
    r = P
    c = int((1 + P) / 2)
    while c != pa:
        if c > pa:
            r = c
            c = int((l + c) / 2)
            cnta += 1

        elif c < pa:
            l = c
            c = int((c + r) / 2)
            cnta += 1

    l = 1
    r = P
    c = int((1 + P) / 2)
    while c != pb:
        if c > pb:
            r = c
            c = int((l + c) / 2)
            cntb += 1
        elif c < pb:
            l = c
            c = int((c + r) / 2)
            cntb += 1

    if cnta > cntb:
        print(f"#{t+1} B")
    elif cnta < cntb:
        print(f"#{t+1} A")
    else:
        print(f"#{t+1} 0")
