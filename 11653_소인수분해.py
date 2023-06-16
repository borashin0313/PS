N = int(input())
K = N
for n in range(2, N+1):
    flag = True
    while(flag):
        if K % n == 0:
            print(n)
            K /= n
        else:
           flag = False
