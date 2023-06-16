while (1):
    N = int(input())
    if N == -1:
        break
    divisor = list([i for i in range(1, N) if N % i == 0 ])
    if sum(divisor) == N :
        print(N, " = " , " + ".join(str(i) for i in divisor), sep="")
    else:
        print(f'{N} is NOT perfect.')
