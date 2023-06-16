N = int(input())

result = 666

while (True):
    if '666' in str(result):
        N -= 1

    if N == 0:
        print(result)
        break
    result += 1
