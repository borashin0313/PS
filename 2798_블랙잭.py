import itertools

N, M = map(int, input().split())
lst = list(map(int, input().split()))

combi_sum = [sum(combi) for combi in list(itertools.combinations(lst,3)) if sum(combi) <= M]
print(max(combi_sum))