N = int(input())
result = 0

for i in range(int(N / 3) + 1):
    for j in range(int(N / 5) + 1):

        if 3 * i + j * 5 == N:
            result = i + j
            break
    if result != 0:
        break
print(result) if result != 0 else print(-1)