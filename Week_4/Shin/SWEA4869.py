arr = [0, 1, 3, 5, 11]
multi = 16
for i in range(5, 31):
    arr.append(arr[i - 2] + multi)
    multi += multi

T = int(input())
for t in range(T):
    N = int(input())
    N //= 10
    print(f"#{t+1} {arr[N]}")
