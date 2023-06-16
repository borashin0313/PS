N = int(input())
numbers = map(int, input().split())
ans = 0
for n in numbers:
    if n == 1:
        continue
    flag = True
    for j in range(2, n):
        if n % j == 0:
            flag = False
    if flag is True:
        ans += 1
print(ans)