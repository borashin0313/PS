N,M = map(int, input().split())
k = 0
ans = 0
for i in range(1, N+1):

    if N % i == 0:
        ans = i
        k += 1
    if k == M:
        break

print(ans) if k == M else print(0)
