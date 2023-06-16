N, M = int(input()), int(input())
ans = []
for n in range(N, M+1):
    if n == 1:
        continue
    flag = True
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    if flag is True:
        ans.append(n)

print(sum(ans), min(ans), sep='\n') if len(ans)>0 else print(-1)
